# 📘 DAY 1 — Docker Fundamentals (Session Notes)

## 1️⃣ Why Containers? (VM vs Containers)

### Traditional Virtual Machines

- **Heavyweight**: each VM includes a full OS + libraries + application
- Slow boot time
- Large resource consumption
- Hard to replicate environments
- Works well for complete OS isolation

### Containers

- Lightweight and fast
- Share the host OS kernel
- Packaged with only the app + dependencies
- Start in milliseconds
- Easier CI/CD integration
- Perfect for microservices

### Key Difference Summary

| Feature | Virtual Machine | Container |
|---------|----------------|-----------|
| Startup time | Minutes | Seconds / ms |
| Resource usage | Heavy | Light |
| OS included | Full OS | Only app runtime & libs |
| Portability | Medium | Very high |
| Ideal for | Monolithic apps | Microservices, DevOps |

## 2️⃣ Docker Architecture: Images, Containers, Layers

### Docker Architecture Components

- **Docker Engine**
  - Core process that builds, runs, and manages containers
- **Images**
  - Read-only templates
  - Used as the blueprint for containers
  - Created using Dockerfiles
  - Layered for efficiency & caching
- **Containers**
  - Running instances of images
  - Lightweight and isolated
  - Can be started, stopped, deleted
- **Layers**
  - Each instruction in a Dockerfile = a new layer
  - Layers are cached → faster rebuilds
  - Shared across containers → saves disk space

### High-Level Docker Flow

```
Dockerfile → Image → Container → Running Application
```

## 3️⃣ Dockerfile Basics

A Dockerfile defines how to build an image.

### Common Dockerfile Instructions

| Instruction | Purpose |
|-------------|---------|
| `FROM` | Base image |
| `WORKDIR` | Set working directory |
| `COPY` | Copy files from host → container |
| `RUN` | Execute commands during build |
| `EXPOSE` | Inform which port app listens on |
| `CMD` | Default command to run container |

### Example Simple Dockerfile

```dockerfile
FROM node:18-alpine
WORKDIR /app
COPY . .
RUN npm install
EXPOSE 3000
CMD ["node", "server.js"]
```

## 4️⃣ Important Docker Commands

### Image Build & Container Run

```bash
docker build -t myapp .
docker run myapp
docker run -d -p 3000:3000 myapp
```

### Container Management

```bash
docker ps           # List running containers
docker ps -a        # List all containers
docker stop <id>    # Stop container
docker rm <id>      # Remove container
```

### Image Management

```bash
docker images       # List images
docker rmi <image>  # Remove image
```

### Debug & Troubleshooting

```bash
docker logs <id>
docker exec -it <id> sh
```

## 5️⃣ Hands-On Lab Exercises

### ✔ Install Docker

- Install Docker Desktop (Windows/Mac)
- Install Docker Engine (Linux)
- Validate:

```bash
docker --version
docker run hello-world
```

### ✔ Build Your First Image

- Create a simple Python or Node.js file (e.g. Hello World API)
- Write a Dockerfile
- Build image using:

```bash
docker build -t hello-api .
```

### ✔ Run Container in Detached Mode

```bash
docker run -d -p 8080:8080 hello-api
```

### ✔ View Logs

```bash
docker logs <container-id>
```

### ✔ Exec into Container

```bash
docker exec -it <container-id> sh
```

## 6️⃣ Mini Project (🔥 Highly Recommended)

### 🔥 Containerize a Simple "Hello API" Microservice

**Steps:**

1. Create a simple web server (Node, Python Flask, or Go)
2. Add an endpoint:

```
GET / → "Hello from Docker!"
```

3. Write a Dockerfile
4. Build the image
5. Run container
6. Test via browser or curl:

```bash
curl http://localhost:8080
```

7. Push to Docker Hub (optional)

**This project teaches:**

- Dockerfile creation
- Image builds
- Container execution
- Port mapping
- Logs, exec, and debugging