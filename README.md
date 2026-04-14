# Besta Veðrið

A weather aggregation system that collects forecasts from multiple sources and always surfaces the best possible weather for any location.

## What it does

Instead of manually checking multiple forecast websites, the system gathers forecast data from several providers, normalizes it into a common format, compares it using a scoring model, and presents the most favorable forecast to the user.

## Providers

- vedur.is
- yr.no
- blika.is
- AccuWeather
- Apple Weather

## Getting Started

```bash
python scripts/bootstrap.py
```

Then copy `.env.example` to `.env` and fill in the required values.

## Utility Scripts

```bash
python scripts/scrape_locations.py
python scripts/seed_locations.py
```

## Development

```bash
pnpm dev
```

## GitHub Actions Runner

This repository is configured to use a self-hosted GitHub Actions runner with the labels:
- `self-hosted`
- `Linux`
- `X64`

That setup is used for CI, Ansible linting, and deployment workflows.

## Structure

| Directory | Purpose |
|---|---|
| `apps/api` | REST API |
| `apps/web` | Frontend |
| `apps/scraper` | Provider scrapers |
| `apps/worker` | Background jobs |
| `packages/scoring-engine` | Forecast comparison logic |
| `packages/shared-types` | Shared TypeScript types |
| `infra/terraform` | Hetzner infrastructure |
| `ansible` | Server configuration and deployment |
| `.github/workflows` | CI and deployment automation |

## Documentation

- [Architecture](docs/architecture.md)
- [Deployment](docs/deployment.md)
- [Scraping Strategy](docs/scraping-strategy.md)
- [Full Project Documentation](docs/doc.md)