# Practical 5b: Run Docker Container and Test Application

## Aim
Run the Docker container for the Flask app and verify it works.

## Prerequisites
- Docker image `flask-app` already built (from 5a)

---

## Step 1: Verify Image Exists
```bash
docker images
```

If missing, rebuild:
```bash
docker build -t flask-app .
```

## Step 2: Run the Container
```bash
docker run -d -p 5000:5000 flask-app
```

| Flag | Meaning |
|------|---------|
| `-d` | Detached (background) mode |
| `-p 5000:5000` | Map host port 5000 → container port 5000 |

## Step 3: Check Running Containers
```bash
docker ps
```

Status should be **Up**.

## Step 4: Test in Browser
Open: http://localhost:5000

Expected: `Welcome to Dockerized Flask Application`

Also try: http://localhost:5000/about

## Step 5: Test with curl (optional)
```bash
curl http://localhost:5000
```

## Step 6: View Logs (if needed)
```bash
docker logs <container_id>
```

## Step 7: Stop the Container
```bash
docker ps                  # get container ID
docker stop <container_id>
```

Or stop all:
```bash
docker stop $(docker ps -q)
```

## Step 8: Remove Container (optional)
```bash
docker rm <container_id>
```
