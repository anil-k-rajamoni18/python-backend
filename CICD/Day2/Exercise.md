# 🔥 Real-Time Hands-On Questions (Docker Intermediate + Compose)

## 1️⃣ Dockerfile Optimization + Multi-Stage Build

### Q1. Convert a simple Node/Python app Dockerfile into a multi-stage build.

**Goal:** Reduce image size by splitting build stage and runtime stage.

**What to confirm:**

- Final image must be smaller
- App should still run on correct port

### Q2. Inspect the size difference between normal image vs multi-stage image.

**Commands to use:**

```bash
docker images
docker history <image>
```

### Q3. Break the build intentionally (e.g., wrong dependency file) and debug it.

**Expected tasks:**

- Read Docker build logs
- Fix COPY order
- Improve caching

## 2️⃣ Volumes (Persistence) Hands-On

### Q4. Run a PostgreSQL container with a named volume for persistence.

**Requirements:**

- Volume must be named `pgdata`
- Data must persist after container deletion
- Confirm using:

```bash
docker volume ls
docker volume inspect pgdata
```

### Q5. Delete the container and verify that data is still available.

**You should:**

- Drop table inside DB
- Restart container
- Check if the table still exists

### Q6. Use a bind mount to edit files live on the host and see updates inside the container.

**Example:**

```bash
docker run -v $(pwd):/app node:18-alpine sh
```

## 3️⃣ Docker Networks Hands-On

### Q7. Create a custom network and run two containers that communicate by name.

**Steps:**

```bash
docker network create appnet
docker run -d --name web --network appnet nginx
docker run -it --name test --network appnet alpine sh
```

Inside `test`:

```bash
ping web
```

### Q8. Inspect the network and list containers inside it.

**Commands:**

```bash
docker network inspect appnet
```

### Q9. Connect one running container to a second network.

**Task:**

```bash
docker network connect appnet <container>
```

## 4️⃣ Environment Variables Hands-On

### Q10. Pass environment variables into a running container and print them.

**Example:**

```bash
docker run -e MODE=dev alpine sh -c "echo $MODE"
```

### Q11. Create an `.env` file and use it with docker compose.

**Steps:**

1. Create `.env`
2. Reference variables in docker-compose.yml
3. Validate using:

```bash
docker compose config
```

## 5️⃣ Docker Compose Hands-On

### Q12. Write a docker-compose.yml that runs a Python/Node API + PostgreSQL.

**Requirements:**

- `api` service
- `db` service
- Shared network
- Volume for database

### Q13. Add port mappings and environment variables.

**Validations:**

- API reachable on localhost
- DB reachable inside API container using service name

### Q14. Run the full application using:

```bash
docker compose up -d
```

**Confirm health:**

```bash
docker compose ps
docker compose logs api
```

### Q15. Tear everything down but keep volumes.

```bash
docker compose down
```

Check if volume still exists.

### Q16. Tear down everything including volumes.

```bash
docker compose down -v
```

## 6️⃣ Multi-Container Debugging Scenarios

### Q17. The API container crashes on startup — investigate the cause.

**You may need:**

```bash
docker compose logs api
docker exec -it api sh
docker inspect api
```

**Possible issues:**

- Wrong DB host
- Missing environment vars
- Port conflicts

### Q18. The DB container refuses connections — fix it.

**Check:**

- Port exposure
- Credentials
- Volume permissions
- Wrong or missing env vars

### Q19. Modify API code locally and confirm that Compose updates automatically with a bind mount.

**Expected Behavior:** Changes in code should reflect instantly without rebuilding.

### Q20. Simulate production mode by scaling API replicas.

```bash
docker compose up --scale api=3 -d
```

**Check:**

```bash
docker compose ps
```