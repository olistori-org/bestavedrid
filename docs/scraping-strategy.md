# Scraping Strategy

## General Approach

Each provider has its own scraper module under `apps/scraper/providers/`. Each module is responsible for:

1. Fetching the page or API response
2. Parsing the response into the normalized `Forecast` schema
3. Returning structured forecast data

## Rate Limiting

- Add delays between requests to avoid triggering bot protection
- Respect `robots.txt` where applicable
- Use browser automation (Playwright) only when a provider requires JavaScript rendering
- Do not run all scrapers simultaneously — stagger requests across providers

## Error Handling

- Retry failed requests with exponential backoff (max 3 retries)
- Log parsing failures with the provider name and URL — do not crash the pipeline
- Mark a provider as temporarily unavailable if it fails consistently
- Partial results are acceptable — always return whatever data was collected

## Normalized Output Schema

All scrapers must output data matching the shared `Forecast` type from `@besta-vedrid/shared-types`:

```typescript
interface Forecast {
  location_id: string;
  location_name: string;
  source: string;          // provider identifier e.g. "vedur.is"
  forecast_time: string;   // ISO 8601
  temperature_c: number;   // Celsius
  wind_ms: number;         // metres per second
  precipitation_mm: number;
  cloud_cover_pct?: number;
  condition?: string;
}
```

## Provider Notes

See `docs/provider-notes/` for individual implementation notes per provider.

## Testing

Each provider module should have unit tests under `apps/scraper/tests/` that:
- Test parsing against a recorded HTML fixture
- Assert the normalized output matches the schema
- Detect breaking changes in page structure early
