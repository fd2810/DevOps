# Practical 6: Docker Compose (Flask + PostgreSQL)

## Aim
a. Create multi-container application using Docker Compose (Flask + PostgreSQL)  
b. Run and test inter-service communication

---

## Project Structure
```
FlaskComposeProject/
├── app.py
├── requirements.txt
├── Dockerfile
├── .env                 (optional)
└── docker-compose.yml
```

---

## Step 1: Create Project Folder
```bash
mkdir FlaskComposeProject
cd FlaskComposeProject
```

## Step 2: Create `app.py`
```python
from flask import Flask
import psycopg2
import os

app = Flask(__name__)

@app.route("/")
def home():
    try:
        conn = psycopg2.connect(
            host=os.getenv("DB_HOST"),
            database=os.getenv("DB_NAME"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD")
        )
        conn.close()
        return "Connected Successfully to PostgreSQL!"
    except Exception as e:
        return "Database Connection Failed: " + str(e)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
```

## Step 3: Create `requirements.txt`
```
Flask
psycopg2-binary
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

## Step 5: Create `docker-compose.yml`
```yaml
version: "3.9"

services:
  web:
    build: .
    container_name: flask_app
    ports:
      - "5000:5000"
    depends_on:
      - db
    environment:
      DB_HOST: db
      DB_NAME: mydatabase
      DB_USER: postgres
      DB_PASSWORD: postgres

  db:
    image: postgres:16
    container_name: postgres_db
    restart: always
    environment:
      POSTGRES_DB: mydatabase
      POSTGRES_USER: postgres
      POSTGRES_PASSWORD: postgres
    ports:
      - "5432:5432"
    volumes:
      - postgres_data:/var/lib/postgresql/data

volumes:
  postgres_data:
```

> Important: Inside Docker, Flask connects to host `db` (service name), **not** `localhost`.

---

## Part (b): Run with Docker Compose

### Build
```bash
docker compose build
```

### Start (detached)
```bash
docker compose up -d
```

### Check containers
```bash
docker ps
```

Both `flask_app` and `postgres_db` should be **Up**.

### Test
Open browser: http://localhost:5000

Expected output:
```
Connected Successfully to PostgreSQL!
```

### View logs
```bash
docker compose logs web
docker compose logs db
```

### Stop
```bash
docker compose down
```

---

## Architecture
```
Browser
   │
   ▼
http://localhost:5000
   │
   ▼
┌────────────────┐
│  Flask (web)   │
│  Container     │
└────────┬───────┘
         │ DB_HOST = db
         ▼
┌────────────────┐
│  PostgreSQL    │
│  Container     │
└────────────────┘
```
