#!/usr/bin/env python3
"""Run the separately installed Astro engine for a daily natal-transit reading."""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_ENGINE = (
    ROOT / ".deps" / "astro" / "skills" / "astrology" / "scripts" / "astro_engine.py"
)


def load_profile(path: Path) -> dict[str, Any]:
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError as exc:
        raise ValueError(f"Profile not found: {path}") from exc
    except json.JSONDecodeError as exc:
        raise ValueError(f"Profile is not valid JSON: {exc}") from exc

    if not isinstance(data, dict):
        raise ValueError("Profile must be a JSON object.")

    required = ("year", "month", "day", "lat", "lng", "tz")
    missing = [key for key in required if key not in data]
    if missing:
        raise ValueError("Profile is missing required fields: " + ", ".join(missing))

    if not isinstance(data["tz"], str) or "/" not in data["tz"]:
        raise ValueError("tz must be an IANA timezone name, e.g. Asia/Singapore.")

    data.setdefault("systems", ["western"])
    if data["systems"] != ["western"]:
        raise ValueError("This skill currently supports Western mode only; set systems to [\"western\"].")

    if data.get("time_known") is False:
        data.pop("hour", None)
        data.pop("minute", None)

    return data


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--profile", required=True, type=Path,
                        help="Path to a private JSON birth profile (never commit it).")
    parser.add_argument("--date", required=True,
                        help="Target local date, YYYY-MM-DD.")
    parser.add_argument("--engine", type=Path, default=DEFAULT_ENGINE,
                        help="Path to upstream astro_engine.py.")
    args = parser.parse_args()

    try:
        from datetime import date
        date.fromisoformat(args.date)
        profile = load_profile(args.profile)
    except (ValueError, TypeError) as exc:
        print(f"Input error: {exc}", file=sys.stderr)
        return 2

    if not args.engine.is_file():
        print(
            f"Astro engine not found: {args.engine}\n"
            "Run: bash scripts/setup.sh",
            file=sys.stderr,
        )
        return 3

    payload = dict(profile)
    payload["mode"] = "transit"
    payload["transit_date"] = args.date

    command = [sys.executable, str(args.engine), "--json", json.dumps(payload)]
    try:
        completed = subprocess.run(
            command, check=False, capture_output=True, text=True, timeout=120
        )
    except subprocess.TimeoutExpired:
        print("Astro engine timed out after 120 seconds.", file=sys.stderr)
        return 4

    if completed.returncode != 0:
        print(completed.stderr.strip() or "Astro engine returned a non-zero exit code.",
              file=sys.stderr)
        return completed.returncode or 5

    try:
        result = json.loads(completed.stdout)
    except json.JSONDecodeError:
        print("Astro engine output was not valid JSON; refusing to interpret it.",
              file=sys.stderr)
        if completed.stderr:
            print(completed.stderr.strip(), file=sys.stderr)
        return 6

    if not isinstance(result, dict):
        print("Astro engine output must be a JSON object.", file=sys.stderr)
        return 7

    # Preserve all engine fields and add a small, explicit request envelope.
    output = {
        "request": {
            "reading_type": "daily_transit",
            "date": args.date,
            "timezone": profile["tz"],
            "zodiac": "western_tropical",
            "requested_systems": ["western"],
        },
        "engine_result": result,
    }
    json.dump(output, sys.stdout, ensure_ascii=False, indent=2)
    sys.stdout.write("\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
