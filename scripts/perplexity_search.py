#!/usr/bin/env python3
"""
Perplexity AI search helper.

Reads PERPLEXITY_API_KEY from environment (auto-loads workspace .env).
Usage:
  python3 scripts/perplexity_search.py "your question here"
  python3 scripts/perplexity_search.py "deep research question" --model sonar-deep-research
  python3 scripts/perplexity_search.py "fast lookup" --model sonar

Models (per https://docs.perplexity.ai):
  sonar               Fast, cheap. Good for quick facts.
  sonar-pro           Balanced. Good default for most research.
  sonar-reasoning-pro Chain-of-thought reasoning. Better for analysis.
  sonar-deep-research Autonomous multi-step research. Slow, expensive, thorough.

Sync vs async:
  sonar-deep-research runs a long autonomous job. A plain synchronous HTTP
  request to /chat/completions gets dropped by the gateway before it finishes
  (RemoteDisconnected). So deep-research is routed through Perplexity's ASYNC
  API automatically: submit the job, get a request id, poll until COMPLETED.
  All other models use the synchronous endpoint (with retry-on-disconnect).
  Note: the async API only accepts sonar-deep-research; other models 400 there,
  which is why routing is automatic and not user-selectable.

Output:
  stdout: synthesized answer followed by a Sources section
  stderr: progress messages (HTTP status, polling, token usage, etc.)
"""

from __future__ import annotations

import argparse
import http.client
import json
import os
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path


PERPLEXITY_API_URL = "https://api.perplexity.ai/chat/completions"
PERPLEXITY_ASYNC_URL = "https://api.perplexity.ai/async/chat/completions"
WORKSPACE_ROOT = Path(__file__).resolve().parent.parent
ENV_FILE = WORKSPACE_ROOT / ".env"

# Errors that mean "the connection dropped, try again" rather than "the request
# was rejected". RemoteDisconnected is raised raw by urllib (not wrapped in
# URLError), so it must be caught explicitly.
TRANSIENT_ERRORS = (
    http.client.RemoteDisconnected,
    http.client.IncompleteRead,
    urllib.error.URLError,
    ConnectionError,
    TimeoutError,
)


def load_env_file(path: Path) -> None:
    """Load KEY=VALUE pairs from a .env file into os.environ.

    Does not override existing env vars (shell wins if both set).
    Handles quoted values, comments, and blank lines. No exotic features.
    """
    if not path.is_file():
        return
    for raw_line in path.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#"):
            continue
        if "=" not in line:
            continue
        key, _, value = line.partition("=")
        key = key.strip()
        value = value.strip()
        if value and value[0] == value[-1] and value[0] in ('"', "'"):
            value = value[1:-1]
        if key and key not in os.environ:
            os.environ[key] = value


def get_api_key() -> str:
    load_env_file(ENV_FILE)
    api_key = os.environ.get("PERPLEXITY_API_KEY")
    if not api_key:
        sys.stderr.write(
            f"ERROR: PERPLEXITY_API_KEY not found.\n"
            f"Add `PERPLEXITY_API_KEY=pplx-your-key-here` to {ENV_FILE}\n"
            f"(workspace .env file, gitignored). See .env.example for the full template.\n"
        )
        sys.exit(2)
    return api_key


def _post(url: str, payload: dict, api_key: str, timeout: int) -> dict:
    req = urllib.request.Request(
        url,
        data=json.dumps(payload).encode("utf-8"),
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
            "Accept": "application/json",
        },
        method="POST",
    )
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        return json.loads(resp.read().decode("utf-8"))


def _get(url: str, api_key: str, timeout: int) -> dict:
    req = urllib.request.Request(
        url,
        headers={
            "Authorization": f"Bearer {api_key}",
            "Accept": "application/json",
        },
        method="GET",
    )
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        return json.loads(resp.read().decode("utf-8"))


def search_sync(query: str, model: str, max_tokens: int, api_key: str, retries: int = 3) -> dict:
    body = {
        "model": model,
        "messages": [{"role": "user", "content": query}],
        "max_tokens": max_tokens,
    }
    sys.stderr.write(f"[perplexity] sync model={model} max_tokens={max_tokens}\n")
    sys.stderr.write(f"[perplexity] query: {query[:120]}{'...' if len(query) > 120 else ''}\n")

    for attempt in range(1, retries + 1):
        try:
            return _post(PERPLEXITY_API_URL, body, api_key, timeout=600)
        except urllib.error.HTTPError as e:
            # An actual HTTP status came back. This is not transient; report and stop.
            sys.stderr.write(f"[perplexity] HTTP {e.code}: {e.read().decode('utf-8', errors='replace')}\n")
            sys.exit(1)
        except TRANSIENT_ERRORS as e:
            reason = getattr(e, "reason", e)
            if attempt < retries:
                wait = 2 ** attempt  # 2s, 4s, 8s
                sys.stderr.write(
                    f"[perplexity] connection dropped ({reason}); "
                    f"retry {attempt}/{retries - 1} in {wait}s\n"
                )
                time.sleep(wait)
                continue
            sys.stderr.write(
                f"[perplexity] connection failed after {retries} attempts: {reason}\n"
                f"[perplexity] if this was sonar-deep-research, it should route to async automatically;\n"
                f"[perplexity] otherwise try --async to use the polling API.\n"
            )
            sys.exit(1)


def search_async(
    query: str,
    model: str,
    max_tokens: int,
    api_key: str,
    poll_interval: int,
    max_wait: int,
) -> dict:
    """Submit a job to the async API and poll until it completes.

    The async create body wraps the request in a "request" object. The poll
    response carries a "status" and, when done, the standard chat completion
    under "response".
    """
    create_body = {
        "request": {
            "model": model,
            "messages": [{"role": "user", "content": query}],
            "max_tokens": max_tokens,
        }
    }
    sys.stderr.write(f"[perplexity] async model={model} max_tokens={max_tokens}\n")
    sys.stderr.write(f"[perplexity] query: {query[:120]}{'...' if len(query) > 120 else ''}\n")

    try:
        created = _post(PERPLEXITY_ASYNC_URL, create_body, api_key, timeout=60)
    except urllib.error.HTTPError as e:
        sys.stderr.write(f"[perplexity] async submit HTTP {e.code}: {e.read().decode('utf-8', errors='replace')}\n")
        sys.exit(1)
    except TRANSIENT_ERRORS as e:
        sys.stderr.write(f"[perplexity] async submit failed: {getattr(e, 'reason', e)}\n")
        sys.exit(1)

    request_id = created.get("id")
    if not request_id:
        sys.stderr.write(f"[perplexity] async submit returned no id: {json.dumps(created)[:300]}\n")
        sys.exit(1)

    sys.stderr.write(f"[perplexity] async job submitted: id={request_id}, polling every {poll_interval}s (max {max_wait}s)\n")
    poll_url = f"{PERPLEXITY_ASYNC_URL}/{request_id}"
    waited = 0
    while waited < max_wait:
        time.sleep(poll_interval)
        waited += poll_interval
        try:
            data = _get(poll_url, api_key, timeout=60)
        except urllib.error.HTTPError as e:
            sys.stderr.write(f"[perplexity] poll HTTP {e.code}: {e.read().decode('utf-8', errors='replace')}\n")
            sys.exit(1)
        except TRANSIENT_ERRORS as e:
            # A dropped poll is harmless; keep polling.
            sys.stderr.write(f"[perplexity] poll hiccup at {waited}s ({getattr(e, 'reason', e)}); continuing\n")
            continue

        status = str(data.get("status", "")).upper()
        sys.stderr.write(f"[perplexity] status={status or 'UNKNOWN'} ({waited}s elapsed)\n")

        if status == "COMPLETED":
            response = data.get("response")
            if response:
                return response
            return data
        if status in ("FAILED", "ERROR", "CANCELLED"):
            msg = data.get("error_message") or data.get("error") or json.dumps(data)[:300]
            sys.stderr.write(f"[perplexity] async job {status}: {msg}\n")
            sys.exit(1)
        # CREATED / PROCESSING / IN_PROGRESS / anything else: keep waiting.

    sys.stderr.write(
        f"[perplexity] async job did not finish within {max_wait}s (id={request_id}).\n"
        f"[perplexity] it may still complete; re-poll GET {poll_url}\n"
    )
    sys.exit(1)


def format_output(data: dict) -> str:
    choices = data.get("choices") or []
    if not choices:
        return json.dumps(data, indent=2)

    answer = choices[0].get("message", {}).get("content", "").strip()

    citations = data.get("citations") or []
    search_results = data.get("search_results") or []

    parts = [answer]

    if search_results:
        parts.append("\n\n## Sources\n")
        for i, sr in enumerate(search_results, 1):
            title = sr.get("title") or sr.get("url") or "(untitled)"
            url = sr.get("url", "")
            parts.append(f"{i}. [{title}]({url})")
    elif citations:
        parts.append("\n\n## Sources\n")
        for i, url in enumerate(citations, 1):
            parts.append(f"{i}. {url}")

    return "\n".join(parts)


def main() -> None:
    parser = argparse.ArgumentParser(description="Perplexity search helper")
    parser.add_argument("query", help="The question or research prompt")
    parser.add_argument(
        "--model",
        default="sonar-pro",
        choices=["sonar", "sonar-pro", "sonar-reasoning-pro", "sonar-deep-research"],
        help="Perplexity model (default: sonar-pro)",
    )
    parser.add_argument("--max-tokens", type=int, default=4000, help="Max output tokens")
    parser.add_argument("--poll-interval", type=int, default=10, help="Async poll interval in seconds (default: 10)")
    parser.add_argument("--max-wait", type=int, default=1800, help="Async max wait in seconds (default: 1800)")
    parser.add_argument("--raw", action="store_true", help="Print raw JSON response")
    args = parser.parse_args()

    api_key = get_api_key()
    use_async = args.model == "sonar-deep-research"

    if use_async:
        data = search_async(
            args.query, args.model, args.max_tokens, api_key,
            poll_interval=args.poll_interval, max_wait=args.max_wait,
        )
    else:
        data = search_sync(args.query, args.model, args.max_tokens, api_key)

    usage = data.get("usage") or {}
    if usage:
        sys.stderr.write(
            f"[perplexity] tokens: prompt={usage.get('prompt_tokens')} "
            f"completion={usage.get('completion_tokens')} total={usage.get('total_tokens')}\n"
        )

    if args.raw:
        print(json.dumps(data, indent=2))
    else:
        print(format_output(data))


if __name__ == "__main__":
    main()
