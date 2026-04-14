# vedur.is

## Access Style
HTML scraping

## Location Source

All available locations are listed at:

```
https://www.vedur.is/vedur/spar/stadaspar
```

This page is the canonical source for location IDs and names used across the system. The `scripts/scrape_locations.py` script targets this URL.

## Forecast Table

vedur.is displays forecast tables per location as HTML. The structure must be inspected and parsed for each location page.

## Implementation Notes

- Parse location links from the listing page
- For each location, fetch the forecast page and extract the table
- Map Icelandic condition labels to normalized condition strings
- Wind data may be in different units — confirm and convert to m/s

## Known Risks

- HTML structure may change without notice
- Add fixture-based tests for known locations
- Monitor for layout changes after site updates
