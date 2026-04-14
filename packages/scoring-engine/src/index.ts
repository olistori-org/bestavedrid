import type { Forecast, BestForecastResult } from "@besta-vedrid/shared-types";

/**
 * Scores a forecast using a simple weighted formula.
 *
 * score =
 *   (temperature_c * 2.0)
 *   - (wind_ms     * 1.5)
 *   - (precipitation_mm * 2.5)
 *   - (cloud_cover_pct  * 0.05)
 */
export function scoreForecast(forecast: Forecast): number {
  return (
    forecast.temperature_c * 2.0 -
    forecast.wind_ms * 1.5 -
    forecast.precipitation_mm * 2.5 -
    (forecast.cloud_cover_pct ?? 0) * 0.05
  );
}

/**
 * Given a list of forecasts for the same location and time slot,
 * returns the best one with its score and explanation.
 */
export function pickBest(forecasts: Forecast[]): BestForecastResult {
  if (forecasts.length === 0) {
    throw new Error("No forecasts provided");
  }

  const scored = forecasts.map((f) => ({ forecast: f, score: scoreForecast(f) }));
  scored.sort((a, b) => b.score - a.score);

  const winner = scored[0];
  const { forecast, score } = winner;

  return {
    location_name: forecast.location_name,
    forecast_time: forecast.forecast_time,
    best_source: forecast.source,
    score,
    temperature_c: forecast.temperature_c,
    wind_ms: forecast.wind_ms,
    precipitation_mm: forecast.precipitation_mm,
    reason: `Highest score (${score.toFixed(1)}) based on temperature, wind, precipitation, and cloud cover`,
  };
}
