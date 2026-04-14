# AccuWeather

## Access Style
Scraping — may require browser automation

## Status
Not yet implemented.

## Implementation Notes

- Some pages require JavaScript rendering — use Playwright
- May have bot protection or rate limiting in place
- Investigate whether a licensed API key would be more reliable than scraping

## Risks

- Bot protection may block automated requests
- HTML structure may change
- Terms of service must be reviewed before production use — scraping may not be permitted
- Consider licensed API access as a more stable alternative

## Licensed API Alternative

AccuWeather offers a developer API. If licensed access is obtained, store credentials in:
- `ACCUWEATHER_API_KEY` GitHub Secret
- Inject via `.env` at runtime
