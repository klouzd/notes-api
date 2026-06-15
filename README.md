# notes-api

Simple REST API for notes build with FastAPI, packaged with Docker. The goal is to practice DevOps methodology: containerization, multi-stage builds, Docker Compose with PostgreSQL, volumes, networks, and healthcheck.

## Stack

- Python 3.12 / FastAPI / Uvicorn
- Docker

## Current Status: Day 1 - basic Docker image

- minimal FastAPI service with 2 endpoints (`/` и `/health`)
- `Dockerfile` with correct layer ordering (requirements are copied and installed separately from the application code, for effective layer caching on rebuilds)

## Roadmap

- **Day 2** - multi-stage build, `.dockerignore`, non-root user, ADD vs COPY
- **Day 3** - `docker-compose.yml` with PostgreSQL, volumes, networks, healthcheck
- **Day 4** - final README, architecture description
