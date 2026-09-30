# Practical 5c: Push Docker Image to Docker Hub

## Aim
Tag the local image and push it to Docker Hub.

## Prerequisites
- Docker Hub account
- Image `flask-app` already built

---

## Step 1: Login to Docker Hub
```bash
docker login
```

Enter your Docker Hub username and password (or Access Token).

Success message: `Login Succeeded`

## Step 2: Tag the Image
Replace `YOUR_USERNAME` with your Docker Hub username:
```bash
docker tag flask-app YOUR_USERNAME/flask-app:latest
```

Example:
```bash
docker tag flask-app nikhita123/flask-app:latest
```

## Step 3: Verify Tag
```bash
docker images
```

You should see both:
- `flask-app`
- `YOUR_USERNAME/flask-app`

## Step 4: Push the Image
```bash
docker push YOUR_USERNAME/flask-app:latest
```

## Step 5: Verify on Docker Hub
1. Go to https://hub.docker.com/
2. Login
3. Click **Repositories**
4. You should see `flask-app`

---

## Useful Commands

| Command | Purpose |
|---------|---------|
| `docker login` | Login to Docker Hub |
| `docker tag <local> <hub/name:tag>` | Tag image |
| `docker push <hub/name:tag>` | Upload image |
| `docker pull <hub/name:tag>` | Download image |
