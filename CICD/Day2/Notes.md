# 📘 DAY 2 — Intermediate Docker + Docker Compose (Session Notes)

## 1️⃣ Dockerfile Optimization (Multi-Stage Builds Intro)

### Why Optimize Dockerfiles?

- Reduce image size
- Improve security (fewer attack surfaces)
- Faster build & deployment times
- Better caching and reuse

### What Are Multi-Stage Builds?

A method that allows you to:

- Use one stage for building the app
- Use a smaller stage for runtime
- Copy only the required binary/artifacts

### Example Multi-Stage Dockerfile

```dockerfile
# Stage 1: Build
FROM node:18-alpine AS build
WORKDIR /app
COPY package*.json .
RUN npm install
COPY . .
RUN npm run build

# Stage 2: Run
FROM node:18-alpine
WORKDIR /app
COPY --from=build /app/dist ./dist
CMD ["node", "dist/server.js"]
```

### Benefits

- Build tools remain in the first stage
- Final image is slimmer & faster
- Best practice for production images

## 2️⃣ Docker Volumes (Persistence)

### Why Do We Need Volumes?

Containers are ephemeral:

- Data is lost when container stops
- Volumes allow persistent storage

### Volume Types

| Volume Type | Description |
|-------------|-------------|
| Named volumes | Managed by Docker, good for DBs |
| Bind mounts | Maps host folder → container folder |
| Tmpfs | In-memory volumes, fast & temporary |

### Commands

```bash
docker volume create myvol
docker run -v myvol:/data ...
docker volume ls
docker volume inspect myvol
```

### Common Use Case

- Databases: MySQL, Postgres need persistent volumes
- Upload folders
- Caches

## 3️⃣ Docker Networks

### Why Docker Networks?

- Allow containers to communicate with each other
- Avoid exposing internal services publicly
- Provide isolated environments

### Network Types

| Type | Description |
|------|-------------|
| bridge | Default; containers communicate inside same network |
| host | Shares host network namespace |
| none | No networking |

### Commands

```bash
docker network create mynet
docker run -d --network mynet --name app nginx
docker network connect
docker network inspect
```

### Container-to-Container Communication

Containers on the same network can reach each other by name.

**Example:**

```
API → postgres:5432
```

## 4️⃣ Environment Variables in Docker

### Why Use Environment Variables?

- Configuration management
- DB connection strings
- Secrets (though better stored in Vault/Secrets Manager)

### Setting Environment Variables

```bash
docker run -e ENV=prod myapp
```

### Using env_file

```bash
docker run --env-file .env myapp
```

### Inside Dockerfile

```dockerfile
ENV PORT=8080
```

## 5️⃣ Docker Compose (Multi-Container Apps)

### Why Docker Compose?

- Define multi-container apps in one file
- Easily bring up pods using `docker compose up`
- Pass env vars, networks, volumes
- Simplifies Dev/Test environments

### Compose File Structure (docker-compose.yml)

```yaml
version: '3.9'
services:
  api:
    build: .
    ports:
      - "8000:8000"
    environment:
      - DB_HOST=postgres
    depends_on:
      - postgres

  postgres:
    image: postgres:15
    environment:
      POSTGRES_PASSWORD: example
    volumes:
      - pgdata:/var/lib/postgresql/data

volumes:
  pgdata:
```

### Key Commands

```bash
docker compose up
docker compose up -d
docker compose down
docker compose logs
docker compose ps
```

## 🧪 Hands-On Labs

### ✔ Add Volume-Based Persistence

Example: PostgreSQL with named volume

```yaml
volumes:
  pgdata:/var/lib/postgresql/data
```

### ✔ Run Multi-Container App (API + DB)

You will run:

- A FastAPI/Python backend
- A PostgreSQL database
- Connected via Docker network via Compose

### ✔ Map Ports & Environment Vars

- Expose API on port 8000
- Use `.env` file for DB credentials
- Use Compose to inject environment variables

Example `.env`:

```
POSTGRES_PASSWORD=passwd123
POSTGRES_USER=admin
```

## 🧱 Mini Project (Highly Practical)

### 🔥 Build a 2-Container Application (FastAPI + PostgreSQL) using Docker Compose

### ✔ Goal

Run a real API connected to a real database using Docker Compose.

### 🚀 Project Structure

```
/project
  ├── api/
  │     ├── app.py
  │     ├── requirements.txt
  │     └── Dockerfile
  └── docker-compose.yml
```

### 🐍 FastAPI Example (app.py)

```python
from fastapi import FastAPI
import psycopg2

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello from FastAPI + Docker Compose!"}
```

### 📝 Dockerfile for FastAPI

```dockerfile
FROM python:3.10-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
```

### 🧩 docker-compose.yml

```yaml
version: "3.9"

services:
  api:
    build: ./api
    ports:
      - "8000:8000"
    depends_on:
      - db
    environment:
      - DB_HOST=db
      - DB_USER=admin
      - DB_PASS=admin123

  db:
    image: postgres:15
    environment:
      POSTGRES_USER: admin
      POSTGRES_PASSWORD: admin123
    volumes:
      - pgdata:/var/lib/postgresql/data

volumes:
  pgdata:
```

### ▶ Run Everything

```bash
docker compose up -d
```

### ✔ Test the API

```bash
curl http://localhost:8000
```