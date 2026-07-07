#!/usr/bin/env python3
"""
Perplexity async submit/poll helper for environments where background processes
do NOT survive across separate shell calls (e.g. Cowork's sandboxed bash, which
reaps processes when each call returns, and caps each call at ~45s).

The trick: sonar-deep-research jobs run on Perplexity's servers. We submit them,
persist the returned request ids to a registry file on disk (which DOES survive
across calls), then poll those ids in later short calls and write each answer to
its output file when COMPLETED. No long-lived local process required.

Usage:
  # 1) Submit a batch described by a manifest JSON file:
  python3 scripts/pplx_async.py submit --registry <reg.json> --manifest <manifest.json>
     manifest.json = [{"label","outfile","model","max_tokens","prompt"}, ...]

  # 2) Poll all pending jobs once (loops internally up to --budget seconds):
  python3 scripts/pplx_async.py poll --registry <reg.json> --budget 35

  # status: print the registry table
  python3 scripts/pplx_async.py status --registry <reg.json>

Reads PERPLEXITY_API_KEY from environment (auto-loads workspace .env).
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

ASYNC_URL = "https://api.perplexity.ai/async/chat/completions"
WORKSPACE_ROOT = Path(__file__).resolve().parent.parent
ENV_FILE = WORKSPACE_ROOT / ".env"

TRANSIENT = (
    http.client.RemoteDisconnected,
    http.client.IncompleteRead,
    urllib.error.URLError,
    ConnectionError,
    TimeoutError,
)


def load_env(path: Path) -> None:
    if not path.is_file():
        return
    for raw in path.read_text(encoding="utf-8").splitlines():
        line = raw.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, _, value = line.partition("=")
        key, value = key.strip(), value.strip()
        if value and value[0] == value[-1] and value[0] in ('"', "'"):
            value = value[1:-1]
        if key and key not in os.environ:
            os.environ[key] = value


def api_key() -> str:
    load_env(ENV_FILE)
    k = os.environ.get("PERPLEXITY_API_KEY")
    if not k:
        sys.stderr.write("ERROR: PERPLEXITY_API_KEY not found in env or .env\n")
        sys.exit(2)
    return k


def _post(url: str, payload: dict, key: str, timeout: int = 60) -> dict:
    req = urllib.request.Request(
        url, data=json.dumps(payload).encode("utf-8"),
        headers={"Authorization": f"Bearer {key}", "Content-Type": "application/json",
                 "Accept": "application/json"}, method="POST")
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        return json.loads(resp.read().decode("utf-8"))


def _get(url: str, key: str, timeout: int = 60) -> dict:
    req = urllib.request.Request(
        url, headers={"Authorization": f"Bearer {key}", "Accept": "application/json"},
        method="GET")
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        return json.loads(resp.read().decode("utf-8"))


def fmt(data: dict) -> str:
    choices = data.get("choices") or []
    if not choices:
        return json.dumps(data, indent=2)
    answer = choices[0].get("message", {}).get("content", "").strip()
    parts = [answer]
    results = data.get("search_results") or []
    cites = data.get("citations") or []
    if results:
        parts.append("\n\n## Sources\n")
        for i, sr in enumerate(results, 1):
            title = sr.get("title") or sr.get("url") or "(untitled)"
            parts.append(f"{i}. [{title}]({sr.get('url','')})")
    elif cites:
        parts.append("\n\n## Sources\n")
        for i, url in enumerate(cites, 1):
            parts.append(f"{i}. {url}")
    return "\n".join(parts)


def load_registry(path: Path) -> list:
    if path.is_file():
        return json.loads(path.read_text(encoding="utf-8"))
    return []


def save_registry(path: Path, reg: list) -> None:
    path.write_text(json.dumps(reg, indent=2), encoding="utf-8")


def cmd_submit(args) -> None:
    key = api_key()
    reg_path = Path(args.registry)
    manifest = json.loads(Path(args.manifest).read_text(encoding="utf-8"))
    reg = load_registry(reg_path)
    done_labels = {j["label"] for j in reg}
    for item in manifest:
        label = item["label"]
        if label in done_labels:
            sys.stderr.write(f"[skip] {label} already in registry\n")
            continue
        body = {"request": {"model": item.get("model", "sonar-deep-research"),
                            "messages": [{"role": "user", "content": item["prompt"]}],
                            "max_tokens": item.get("max_tokens", 8000)}}
        try:
            created = _post(ASYNC_URL, body, key)
        except urllib.error.HTTPError as e:
            sys.stderr.write(f"[err] {label} submit HTTP {e.code}: {e.read().decode('utf-8','replace')[:200]}\n")
            continue
        except TRANSIENT as e:
            sys.stderr.write(f"[err] {label} submit failed: {getattr(e,'reason',e)}\n")
            continue
        rid = created.get("id")
        reg.append({"label": label, "id": rid, "outfile": item["outfile"],
                    "model": item.get("model", "sonar-deep-research"), "status": "SUBMITTED"})
        save_registry(reg_path, reg)
        sys.stderr.write(f"[ok] submitted {label} id={rid}\n")
    print(f"registry now has {len(reg)} jobs at {reg_path}")


def cmd_poll(args) -> None:
    key = api_key()
    reg_path = Path(args.registry)
    reg = load_registry(reg_path)
    deadline = time.time() + args.budget
    pending = [j for j in reg if j.get("status") != "COMPLETED"]
    while pending and time.time() < deadline:
        for job in pending:
            try:
                data = _get(f"{ASYNC_URL}/{job['id']}", key)
            except (urllib.error.HTTPError,) + TRANSIENT as e:
                sys.stderr.write(f"[poll] {job['label']} hiccup: {e}\n")
                continue
            status = str(data.get("status", "")).upper()
            job["status"] = status or job.get("status")
            if status == "COMPLETED":
                resp = data.get("response") or data
                Path(job["outfile"]).parent.mkdir(parents=True, exist_ok=True)
                Path(job["outfile"]).write_text(fmt(resp), encoding="utf-8")
                sys.stderr.write(f"[done] {job['label']} -> {job['outfile']}\n")
            elif status in ("FAILED", "ERROR", "CANCELLED"):
                sys.stderr.write(f"[fail] {job['label']} status={status}\n")
        save_registry(reg_path, reg)
        pending = [j for j in reg if j.get("status") not in ("COMPLETED", "FAILED", "ERROR", "CANCELLED")]
        if pending:
            time.sleep(args.interval)
    # summary
    done = sum(1 for j in reg if j.get("status") == "COMPLETED")
    print(f"{done}/{len(reg)} completed")
    for j in reg:
        print(f"  {j.get('status','?'):12} {j['label']}")
    sys.exit(0 if done == len(reg) else 3)


def cmd_status(args) -> None:
    reg = load_registry(Path(args.registry))
    done = sum(1 for j in reg if j.get("status") == "COMPLETED")
    print(f"{done}/{len(reg)} completed")
    for j in reg:
        print(f"  {j.get('status','?'):12} {j['label']}  ({j.get('outfile')})")


def main() -> None:
    p = argparse.ArgumentParser(description="Perplexity async submit/poll helper")
    sub = p.add_subparsers(dest="cmd", required=True)

    s = sub.add_parser("submit")
    s.add_argument("--registry", required=True)
    s.add_argument("--manifest", required=True)
    s.set_defaults(func=cmd_submit)

    q = sub.add_parser("poll")
    q.add_argument("--registry", required=True)
    q.add_argument("--budget", type=int, default=35, help="max seconds this call will poll")
    q.add_argument("--interval", type=int, default=8, help="seconds between poll rounds")
    q.set_defaults(func=cmd_poll)

    t = sub.add_parser("status")
    t.add_argument("--registry", required=True)
    t.set_defaults(func=cmd_status)

    args = p.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
