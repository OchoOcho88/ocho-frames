#!/usr/bin/env python3
"""Generate a voiceover with ElevenLabs (premium, natural TTS).

Reads ELEVENLABS_API_KEY (and optional ELEVENLABS_VOICE_ID) from .env.
Zero third-party deps (urllib only), so it runs on the system python.

Usage:
    python3 scripts/elevenlabs_tts.py "Everyday training, elevated." -o vo.mp3
    python3 scripts/elevenlabs_tts.py "..." --voice-id <id> --model eleven_multilingual_v2
    python3 scripts/elevenlabs_tts.py --list          # list the voices on your account

The output is mp3; ffmpeg can mux it straight into a render, e.g.
    ffmpeg -i video.mp4 -i vo.mp3 -c:v copy -c:a aac -shortest out.mp4
"""
import argparse
import json
import os
import sys
import urllib.error
import urllib.request

API = "https://api.elevenlabs.io/v1"
# Default: "Sarah" — a warm, soft female voice available on all accounts.
DEFAULT_VOICE_ID = "EXAVITQu4vr4xnSDxMaL"
DEFAULT_MODEL = "eleven_multilingual_v2"


def load_env(path):
    """Minimal .env parser (KEY=VALUE lines), no dependency on python-dotenv."""
    env = {}
    if os.path.exists(path):
        with open(path) as f:
            for line in f:
                line = line.strip()
                if not line or line.startswith("#") or "=" not in line:
                    continue
                k, v = line.split("=", 1)
                env[k.strip()] = v.strip().strip('"').strip("'")
    return env


def get_key(env):
    key = os.environ.get("ELEVENLABS_API_KEY") or env.get("ELEVENLABS_API_KEY")
    if not key or key in ("", "..."):
        sys.exit("No ELEVENLABS_API_KEY set. Add it to .env (get one at "
                 "https://elevenlabs.io/app/settings/api-keys).")
    return key


def list_voices(key):
    req = urllib.request.Request(f"{API}/voices", headers={"xi-api-key": key})
    with urllib.request.urlopen(req) as r:
        data = json.load(r)
    for v in data.get("voices", []):
        labels = v.get("labels", {}) or {}
        desc = ", ".join(f"{k}={val}" for k, val in labels.items())
        print(f"{v['voice_id']}  {v['name']:<18} {desc}")


def synth(key, text, voice_id, model, out):
    body = json.dumps({
        "text": text,
        "model_id": model,
        "voice_settings": {"stability": 0.5, "similarity_boost": 0.75, "style": 0.0},
    }).encode()
    url = f"{API}/text-to-speech/{voice_id}?output_format=mp3_44100_128"
    req = urllib.request.Request(url, data=body, headers={
        "xi-api-key": key,
        "Content-Type": "application/json",
        "Accept": "audio/mpeg",
    })
    try:
        with urllib.request.urlopen(req) as r:
            audio = r.read()
    except urllib.error.HTTPError as e:
        sys.exit(f"ElevenLabs API error {e.code}: {e.read().decode(errors='replace')}")
    with open(out, "wb") as f:
        f.write(audio)
    print(f"wrote {out} ({len(audio)/1024:.0f} KB)")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("text", nargs="?", help="Text to speak")
    ap.add_argument("-o", "--output", default="vo.mp3")
    ap.add_argument("--voice-id", default=None)
    ap.add_argument("--model", default=DEFAULT_MODEL)
    ap.add_argument("--list", action="store_true", help="List voices on your account")
    args = ap.parse_args()

    repo = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    env = load_env(os.path.join(repo, ".env"))
    key = get_key(env)

    if args.list:
        list_voices(key)
        return
    if not args.text:
        ap.error("provide text to speak (or --list)")
    voice_id = args.voice_id or os.environ.get("ELEVENLABS_VOICE_ID") \
        or env.get("ELEVENLABS_VOICE_ID") or DEFAULT_VOICE_ID
    synth(key, args.text, voice_id, args.model, args.output)


if __name__ == "__main__":
    main()
