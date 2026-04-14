#!/usr/bin/env python3
from __future__ import annotations

import json
import re
import sys
import unicodedata
from html.parser import HTMLParser
from typing import Any
from urllib.parse import urljoin
from urllib.request import urlopen


VEDUR_LOCATIONS_URL = "https://www.vedur.is/vedur/spar/stadaspar"


def slugify(value: str) -> str:
    normalized = unicodedata.normalize("NFKD", value)
    ascii_value = normalized.encode("ascii", "ignore").decode("ascii")
    lowered = ascii_value.lower().strip()
    return re.sub(r"[^a-z0-9]+", "-", lowered).strip("-")


class LocationParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.in_anchor = False
        self.current_href = ""
        self.current_text: list[str] = []
        self.locations: list[dict[str, str]] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag != "a":
            return
        attributes = dict(attrs)
        href = attributes.get("href")
        if not href:
            return
        if "/vedur/spar/" not in href:
            return
        self.in_anchor = True
        self.current_href = href
        self.current_text = []

    def handle_data(self, data: str) -> None:
        if self.in_anchor:
            self.current_text.append(data)

    def handle_endtag(self, tag: str) -> None:
        if tag != "a" or not self.in_anchor:
            return
        name = " ".join(part.strip() for part in self.current_text if part.strip()).strip()
        href = self.current_href
        self.in_anchor = False
        self.current_href = ""
        self.current_text = []

        if not name:
            return

        url = urljoin(VEDUR_LOCATIONS_URL, href)
        location = {
            "id": slugify(name),
            "name": name,
            "url": url,
        }
        if location not in self.locations:
            self.locations.append(location)


def fetch_html(url: str) -> str:
    with urlopen(url) as response:
        return response.read().decode("utf-8", errors="replace")


def main() -> int:
    print(f"Fetching locations from {VEDUR_LOCATIONS_URL}...", file=sys.stderr)
    html = fetch_html(VEDUR_LOCATIONS_URL)

    parser = LocationParser()
    parser.feed(html)

    locations: list[dict[str, Any]] = parser.locations
    print(f"Found {len(locations)} candidate locations", file=sys.stderr)
    print(json.dumps(locations, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())