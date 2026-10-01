# Practical 5a: Write Dockerfile and Build Docker Image

## Aim
Write a Dockerfile for a Flask application and build a Docker image.

## Prerequisites
- Docker Desktop installed and running
- Flask application ready

---

## Step 1: Create Project Folder
```bash
mkdir Flask_Project
cd Flask_Project
```

## Step 2: Create `app.py`
```python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to Dockerized Flask Application"

@app.route('/about')
def about():
    return "Docker Practical"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
```

## Step 3: Create `requirements.txt`
```
Flask
```

## Step 4: Create `Dockerfile`
```dockerfile
FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["python", "app.py"]
```

### Explanation of Dockerfile

| Instruction | Purpose |
|-------------|---------|
| `FROM` | Base image (Python 3.12) |
| `WORKDIR` | Working directory inside container |
| `COPY requirements.txt` | Copy dependency file |
| `RUN pip install` | Install packages |
| `COPY . .` | Copy all project files |
| `EXPOSE 5000` | Document the port |
| `CMD` | Command to start the app |

## Step 5: Project Structure
```
Flask_Project/
├── app.py
├── Dockerfile
└── requirements.txt
```

## Step 6: Build the Image
```bash
1. docker build -t flask-app .  //if the command is running from the same folder where the file is there
for example: 
C:\Users\Intel\Desktop\College\DevOps\devops-practicals\practical-05-docker\05a-dockerfile>docker build -t flask .
2. docker build -t flask-app practical-05-docker/05a-dockerfile   // if the command is running from other folder rather then where is the file u should add path instead of '.'
for example :
C:\Users\Intel\Desktop\College\DevOps\devops-practicals> docker build -t flask-app practical-05-docker/05a-dockerfile

```

## Step 7: Verify Image
```bash
docker images
```

You should see `flask-app` in the list.

---

## Common Errors

| Error | Solution |
|-------|----------|
| `docker: command not found` | Start Docker Desktop |
| `Dockerfile not found` | Run command from correct folder |
| Build fails on packages | Check internet + requirements.txt |
