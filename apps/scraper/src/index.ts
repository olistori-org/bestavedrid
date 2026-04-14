export type ScraperHealth = {
  service: "scraper";
  status: "ok";
};

export function getScraperHealth(): ScraperHealth {
  return { service: "scraper", status: "ok" };
}
