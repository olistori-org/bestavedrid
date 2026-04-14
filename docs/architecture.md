# Architecture

## Overview

The system is built around a data pipeline that collects, normalizes, scores, and serves weather forecasts.

```
[Source Scrapers / API Collectors]
              ↓
      [Normalization Layer]
              ↓
      [Storage / Cache Layer]
              ↓
     [Comparison / Scoring Engine]
              ↓
       [API / Web Application]
              ↓
            [User]
```

## Services

### api
REST API for search, forecast retrieval, and comparison results. Served to the web frontend and any external consumers.

### web
Frontend UI. The user-facing application for searching locations and viewing best weather results.

### scraper
Collects weather data from all providers and normalizes it into the shared schema. Runs on a schedule triggered by the worker.

### worker
Background job runner using BullMQ. Handles scheduled collection, cache refresh, and comparison updates.

### postgres
Primary data store for normalized forecast data and location records.

### redis
Used as a cache layer and job queue backend for the worker.

### traefik
Reverse proxy providing HTTPS termination and routing to all HTTP services.

## Data Flow

1. The worker triggers scraper jobs on a schedule
2. The scraper collects forecasts from each provider
3. Forecasts are normalized into the shared `Forecast` schema
4. The scoring engine compares normalized forecasts per location and time slot
5. Results are stored in postgres and cached in redis
6. The API reads stored results and serves them to the web frontend

## Normalized Data Model

```typescript
interface Forecast {
  location_id: string;
  location_name: string;
  source: string;
  forecast_time: string; // ISO 8601
  temperature_c: number;
  wind_ms: number;
  precipitation_mm: number;
  cloud_cover_pct?: number;
  condition?: string;
}
```

## Scoring Model

```
score =
  (temperature_c * 2.0)
  - (wind_ms     * 1.5)
  - (precipitation_mm * 2.5)
  - (cloud_cover_pct  * 0.05)
```

The provider with the highest score for a given location and time slot is selected as the best forecast.
