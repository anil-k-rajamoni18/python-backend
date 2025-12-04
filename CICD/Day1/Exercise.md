# 🔥 Real-Time Docker Hands-On Questions (With Expected Outcomes)

## 1️⃣ Basic Commands & Container Management

### Q1. Run an Nginx container and expose it on port 8080.

**Task:**

```bash
docker run -d -p 8080:80 nginx
```

**Expected Outcome:**

Nginx container should run in detached mode and serve the welcome page at:
```
http://localhost:8080
```

### Q2. List all running containers.

**Task:**

```bash
docker ps
```

**Outcome:** See only active containers.

### Q3. List all containers including stopped ones.

**Task:**

```bash
docker ps -a
```

### Q4. Stop a running container.

**Task:**

```bash
docker stop <container-id>
```

### Q5. Remove a stopped container.

**Task:**

```bash
docker rm <container-id>
```

## 2️⃣ Dockerfile & Image Building

### Q6. Create a simple Node.js "Hello World" API and Dockerize it.

**Tasks:**

Create `server.js`:

```javascript
console.log("Server running...");
```

Create a Dockerfile:

```dockerfile
FROM node:18-alpine
COPY . .
CMD ["node", "server.js"]
```

Build:

```bash
docker build -t hello-node .
```

Run:

```bash
docker run hello-node
```

**Outcome:** Should print `Server running...`

### Q7. Modify the Dockerfile to use a working directory.

**Task:**

```dockerfile
WORKDIR /app
```

**Outcome:** Files are copied into `/app` inside the container.

### Q8. Build an image with a custom tag (eg: v1).

**Task:**

```bash
docker build -t myimage:v1 .
```

## 3️⃣ Debugging & Troubleshooting

### Q9. View logs of a running container.

**Task:**

```bash
docker logs <id>
```

### Q10. Exec into a container shell.

**Task:**

```bash
docker exec -it <id> sh
```

**Outcome:** You should be inside container terminal.

## 4️⃣ Image & Storage Experiments

### Q11. Show all images on your system.

**Task:**

```bash
docker images
```

### Q12. Remove an image.

**Task:**

```bash
docker rmi <image-id>
```

**Note:** Must remove containers created from that image first.

### Q13. Pull an image from Docker Hub.

**Task:**

```bash
docker pull redis
```

### Q14. Run Redis in interactive mode.

**Task:**

```bash
docker run -it redis sh
```

## 5️⃣ Networking Hands-On

### Q15. Run two containers and ping one from another.

Create a custom network:

```bash
docker network create mynet
```

Start containers:

```bash
docker run -d --name c1 --network mynet nginx
docker run -it --name c2 --network mynet alpine sh
```

Inside c2, ping c1:

```bash
ping c1
```

## 6️⃣ Practical Microservice Scenario

### Q16. Build & run a containerized "Hello API".

Same as the mini project:

1. Create code
2. Write Dockerfile
3. Build image
4. Run with port mapping
5. Test with curl

**Expected Output:**

```
Hello from Docker!
```

## 7️⃣ Real Deployment-Like Questions

### Q17. Your container exits immediately — how do you troubleshoot it?

Try:

```bash
docker logs <id>
docker inspect <id>
docker run -it <image> sh
```

### Q18. How do you see CPU/memory usage of containers?

**Task:**

```bash
docker stats
```

### Q19. How do you copy files from host → container?

**Task:**

```bash
docker cp file.txt <container>:/location
```

### Q20. How do you copy files from container → host?

**Task:**

```bash
docker cp <container>:/path/file.txt .
```