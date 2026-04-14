#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path


INITIAL_LOCATIONS = [
    {"id": "reykjavik", "name": "Reykjavik", "country": "IS"},
    {"id": "akureyri", "name": "Akureyri", "country": "IS"},
    {"id": "selfoss", "name": "Selfoss", "country": "IS"},
    {"id": "keflavik", "name": "Keflavik", "country": "IS"},
    {"id": "isafjordur", "name": "Isafjordur", "country": "IS"},
]


def main() -> int:
    output_path = Path(__file__).resolve().parent / "seed_locations.json"
    output_path.write_text(
        json.dumps(INITIAL_LOCATIONS, indent=2),
        encoding="utf-8",
    )

    print(f"Wrote {len(INITIAL_LOCATIONS)} locations to {output_path.name}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())