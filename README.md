# notes-api

Simple REST API for notes made on top of FastAPI, packed in Docker. The goal is to learn DevOps methodology and practice: containerization, multi-stage builds, Docker Compose with PostgreSQL, volumes, networks, and healthcheck.

## Stack

- Python 3.12 / FastAPI / Uvicorn
- Docker

## Actual Status: Day 1 - basic docker image

- minimal FastAPI-service with 2 endpoints (`/` и `/health`)
- `Dockerfile` with the correct layers order (requirements copy and installed separately from the code - for effective caching and rebuilds)

## Roadmap

- **Day 2** - multi-stage build, `.dockerignore`, non-root user, ADD vs COPY
- **Day 3** - `docker-compose.yml` with PostgreSQL, volumes, networks, healthcheck
- **Day 4** - final README, architecture description
