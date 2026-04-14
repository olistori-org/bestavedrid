# yr.no

## Access Style
Official API

## API

yr.no provides structured JSON forecast data via their public API. Documentation:

```
https://developer.yr.no/
```

## Implementation Notes

- Use the locationforecast endpoint for point forecasts
- Data is available in JSON format — no HTML scraping required
- Coordinates (lat/lon) are required — map internal location IDs to coordinates
- Review terms of service and attribution requirements before production use

## Data Mapping

| yr.no field | Normalized field |
|---|---|
| `air_temperature` | `temperature_c` |
| `wind_speed` | `wind_ms` |
| `precipitation_amount` | `precipitation_mm` |
| `cloud_area_fraction` | `cloud_cover_pct` |

## Known Risks

- API rate limits — check the fair use policy
- Location coordinate mapping must be maintained
