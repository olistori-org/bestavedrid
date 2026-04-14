// Normalized forecast data model shared across all apps and packages

export interface Forecast {
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

export interface Location {
  id: string;
  name: string;
  country: string;
}

export interface BestForecastResult {
  location_name: string;
  forecast_time: string;
  best_source: string;
  score: number;
  temperature_c: number;
  wind_ms: number;
  precipitation_mm: number;
  reason: string;
}
