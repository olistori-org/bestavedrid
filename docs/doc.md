# Besta Veðrið – Project Documentation

## Overview

**Besta Veðrið** is a weather aggregation system that collects forecasts from multiple sources and determines the best possible weather across them.

The core idea is simple:

> Always show the best weather available across all providers for any given location.

Instead of manually checking multiple forecast websites, the system should gather the available forecast data, normalize it into a common format, compare it, and present the most favorable forecast to the user.

---

## Goals

- Aggregate weather data from multiple providers:
  - vedur.is
  - blika.is
  - yr.no
  - accuweather.com
  - Apple Weather
- Support searching across all locations available from:
  - https://www.vedur.is/vedur/spar/stadaspar
- Parse and display forecast tables for each source when available
- Compare forecasts and determine the best weather across all providers
- Always show the best forecast result, even when it comes from a different provider than the others
- Keep the system maintainable, automatable, and deployable through GitHub, GitHub Actions, Docker, and Ansible

---

## Product Vision

The meaning of **Besta Veðrið** is that the system should always surface the forecast that looks best among all the supported weather services.

Examples:

- If AccuWeather shows less wind and less rain than the other providers, then AccuWeather should be shown as the best option
- If vedur.is shows better temperature and no precipitation while the others predict rain, then vedur.is should be selected
- If one provider has the best overall score for a location and time window, that provider becomes the displayed result

The product is not only a weather scraper. It is a **forecast comparison engine**.

---

## Data Sources

| Source | Access Style | Notes |
|---|---|---|
| vedur.is | Scraping | Important Icelandic source, especially for locations and forecast tables |
| blika.is | Scraping or API if available | Needs investigation for stable access |
| yr.no | API and page data | Usually structured and reliable |
| AccuWeather | Scraping | May require browser automation for some pages |
| Apple Weather | API or integration layer | Availability depends on access method and credentials |

---

## Core Features

### 1. Location Search

The system should collect all locations listed on the vedur.is location forecast page and make them searchable.

Requirements:

- Scrape all locations from the vedur.is location listing
- Store them in a normalized structure
- Support:
  - search by location name
  - exact match and partial match
  - autocomplete later if needed
- Connect weather-source-specific location mapping to the normalized location record

### 2. Forecast Collection

Each provider should have its own collector or scraper.

Examples:

- vedur.is: parse HTML forecast tables
- yr.no: consume official structured data when available
- AccuWeather: scrape forecast pages
- blika.is: inspect structure and implement parser
- Apple Weather: integrate through supported API path if available

Each source should output data into a shared schema.

### 3. Forecast Table View

For a selected location, the user should be able to:

- inspect each source individually
- view forecast tables when the provider offers them
- compare forecast values side by side

### 4. Best Weather Comparison

The system should compare providers for the same location and time slot.

The comparison should consider:

- temperature
- wind speed
- precipitation
- cloud cover or sunshine when available
- optional comfort score

The result should identify:

- best source
- reason why it was selected
- underlying values used for the decision

---

## Normalized Data Model

All forecast data should be converted into a unified format.

Example:

```json
{
  "location_id": "reykjavik",
  "location_name": "Reykjavik",
  "source": "yr.no",
  "forecast_time": "2026-04-08T12:00:00Z",
  "temperature_c": 8,
  "wind_ms": 3,
  "precipitation_mm": 0,
  "cloud_cover_pct": 20,
  "condition": "Partly cloudy"
}
```

Normalization rules:

- temperature in Celsius
- wind in m/s
- precipitation in mm
- timestamps in ISO 8601
- location references mapped to internal IDs

---

## Best Weather Scoring

A first scoring model can be simple and adjusted later.

Example concept:

```text
score =
  (temperature_c * 2.0)
  - (wind_ms * 1.5)
  - (precipitation_mm * 2.5)
  - (cloud_cover_pct * 0.05)
```

Possible improvements later:

- user-defined weights
- separate summer and winter profiles
- hiking / travel / photography modes
- confidence scoring by source

The selected output should always include both:

- the winning provider
- the comparison explanation

Example:

```json
{
  "location_name": "Reykjavik",
  "forecast_time": "2026-04-08T12:00:00Z",
  "best_source": "accuweather",
  "score": 14.8,
  "temperature_c": 10,
  "wind_ms": 2,
  "precipitation_mm": 0,
  "reason": "Highest temperature with lowest wind and no precipitation"
}
```

---

## Suggested Architecture

```text
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

---

## Suggested Repository Structure

This structure is designed for Git, GitHub Actions, Docker, and Ansible.

```text
besta-vedrid/
├── .github/
│   └── workflows/
│       ├── ci.yml
│       ├── deploy.yml
│       └── ansible-lint.yml
├── ansible/
│   ├── inventories/
│   │   ├── prod/
│   │   │   ├── hosts.ini
│   │   │   └── group_vars/
│   │   │       └── all.yml
│   │   └── dev/
│   │       ├── hosts.ini
│   │       └── group_vars/
│   │           └── all.yml
│   ├── playbooks/
│   │   ├── bootstrap-server.yml
│   │   ├── deploy-app.yml
│   │   └── docker-host.yml
│   ├── roles/
│   │   ├── common/
│   │   ├── docker/
│   │   ├── traefik/
│   │   ├── app/
│   │   ├── postgres/
│   │   └── redis/
│   ├── ansible.cfg
│   └── requirements.yml
├── infra/
│   └── terraform/
│       ├── environments/
│       │   ├── prod/
│       │   │   ├── main.tf
│       │   │   ├── variables.tf
│       │   │   ├── outputs.tf
│       │   │   ├── versions.tf
│       │   │   └── terraform.tfvars.example
│       │   └── dev/
│       │       ├── main.tf
│       │       ├── variables.tf
│       │       ├── outputs.tf
│       │       ├── versions.tf
│       │       └── terraform.tfvars.example
│       └── modules/
│           ├── hetzner-server/
│           ├── firewall/
│           ├── volume/
│           └── networking/
├── docker/
│   ├── app/
│   │   └── Dockerfile
│   ├── scraper/
│   │   └── Dockerfile
│   ├── worker/
│   │   └── Dockerfile
│   └── reverse-proxy/
│       └── Dockerfile
├── apps/
│   ├── api/
│   │   ├── src/
│   │   ├── tests/
│   │   ├── Dockerfile
│   │   └── package.json
│   ├── web/
│   │   ├── src/
│   │   ├── public/
│   │   ├── tests/
│   │   └── package.json
│   ├── scraper/
│   │   ├── src/
│   │   ├── providers/
│   │   │   ├── vedur/
│   │   │   ├── blika/
│   │   │   ├── yr/
│   │   │   ├── accuweather/
│   │   │   └── apple_weather/
│   │   ├── tests/
│   │   └── package.json
│   └── worker/
│       ├── src/
│       ├── tests/
│       └── package.json
├── packages/
│   ├── shared-types/
│   ├── config/
│   ├── utils/
│   └── scoring-engine/
├── scripts/
│   ├── bootstrap.py
│   ├── scrape_locations.py
│   └── seed_locations.py
├── docs/
│   ├── doc.md
│   ├── architecture.md
│   ├── deployment.md
│   ├── scraping-strategy.md
│   └── provider-notes/
│       ├── vedur.md
│       ├── blika.md
│       ├── yr.md
│       ├── accuweather.md
│       └── apple-weather.md
├── .env.example
├── .gitignore
├── docker-compose.yml
├── README.md
├── package.json
└── pnpm-workspace.yaml
```

---

## Why This Structure

### apps/
Contains the actual runnable services.

- `api/`: backend API for search, forecasts, and comparison results
- `web/`: frontend UI
- `scraper/`: collects weather data from all sources
- `worker/`: background jobs, scheduled comparisons, and refresh tasks

### packages/
Contains shared code reused by the apps.

- shared types
- config parsing
- reusable helpers
- scoring engine

### infra/terraform/
Contains the infrastructure code for Hetzner.

- separate environments for dev and prod
- reusable modules for servers and firewalls
- easy to run from GitHub Actions later

### ansible/
Contains server configuration and deployment automation.

Use it for:

- installing Docker
- installing Docker Compose plugin if needed
- configuring system users
- setting up reverse proxy
- setting up app containers
- provisioning PostgreSQL or Redis hosts if you keep them on the VPS

### docs/
Keeps project documentation inside Git.

### .github/workflows/
Stores CI and deployment workflows.

---

## Git and Secrets Strategy

### Store in Git

Commit:

- application code
- infrastructure code
- Ansible playbooks and roles
- docs
- Dockerfiles
- workflow files
- `.env.example`

Do not commit:

- `.env`
- real API keys
- SSH private keys
- Terraform state
- Ansible vault secrets unless intentionally managed that way

### Store in GitHub Secrets

Examples:

- `HCLOUD_TOKEN`
- `APPLE_WEATHER_*` credentials if needed
- `ACCUWEATHER_*` credentials if using licensed access
- `ANSIBLE_VAULT_PASSWORD` if you later use Ansible Vault
- app secrets such as database passwords or JWT keys

If deployment is executed from the self-hosted GitHub runner installed directly on the VPS, SSH deploy secrets are not required for the default workflow.

GitHub Actions should read the secrets at runtime and inject them into the workflows.

---

## GitHub Actions Plan

You want GitHub Actions for automation. A good first setup is:

### ci.yml
Runs on push and pull request.

Tasks:

- install dependencies
- lint
- run tests
- build app images or app packages
- optionally run scraper unit tests

### deploy.yml
Runs on push to main or manual dispatch.

Tasks:

- authenticate using GitHub secrets
- run Terraform plan or apply for infrastructure changes when needed
- run Ansible against the VPS
- deploy or update Docker containers

### ansible-lint.yml
Runs ansible-lint on playbooks and roles.

---

## Ansible Role Strategy

Since you want Ansible to set up the Docker environment, this is a good role split:

### common
- system packages
- timezone
- base users
- SSH hardening if needed

### docker
- install Docker Engine
- install Docker Compose plugin
- ensure Docker service is enabled
- allow deploy user access to Docker

### traefik or nginx
- reverse proxy
- HTTPS termination
- routing to app containers

### app
- create app directory
- copy compose files or templates
- log in to registry if needed
- run `docker compose pull`
- run `docker compose up -d`

### postgres
Optional if database is on the same server.

### redis
Optional if cache/queue is on the same server.

---

## Suggested Deployment Model

### VPS Base Layer
Provision with Terraform:

- Hetzner server
- firewall
- SSH key
- optional volume
- DNS records later if needed

### Configuration Layer
Configure with Ansible:

- install Docker
- install reverse proxy
- create deploy directories
- write env files from secrets
- deploy containers

### Application Layer
Run with Docker:

- API container
- scraper container
- worker container
- web container
- database container if self-hosted
- Redis container if needed

---

## Recommended Initial Docker Services

For a solid MVP, you likely need:

- `api`
- `scraper`
- `worker`
- `web`
- `postgres`
- `redis`
- `traefik` or `nginx`

You may choose to skip some at first, but this is a sensible target architecture.

---

## Roadmap

### Phase 1 – MVP
- Git repo initialized
- Terraform for Hetzner server
- Ansible installs Docker
- single scraper for vedur.is
- normalized location storage
- basic API endpoint

### Phase 2
- add yr.no
- add comparison engine
- store comparison results
- basic frontend for search and results

### Phase 3
- add blika.is
- add AccuWeather
- improve scoring and comparison explanations
- GitHub Actions deployment pipeline

### Phase 4
- Apple Weather integration
- alerts and saved searches
- user preferences for scoring
- better observability and monitoring

---

## Key Technical Risks

- HTML structure changes on scraped sites
- rate limiting or bot protection
- provider terms of service
- mismatch in location naming across providers
- time-slot differences between forecast sources
- Apple Weather access complexity

---

## Recommendation for First Implementation

Start small:

1. Set up Git repo
2. Add Terraform for Hetzner
3. Add Ansible role for Docker host setup
4. Deploy one API container and one scraper container
5. Support vedur.is location scraping first
6. Add yr.no second
7. Build the scoring engine only after normalized data is stable

This will keep the project manageable and reduce early complexity.

---

## Definition of Success

The project is successful when a user can:

- search for a location
- inspect forecast data from multiple providers
- see which provider currently offers the best weather
- understand why that provider was selected
- trust that the system updates automatically on the VPS through GitHub Actions and Ansible

---

## Final Vision Statement

**Besta Veðrið** should become a single place where you can compare multiple weather services and instantly see the best forecast for any supported location.

It should remove the need to manually check several sites and make the comparison clear, fast, and explainable.
