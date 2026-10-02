# Practical 10: Dockerize 3-Tier Application with Docker Compose

## Aim
Dockerize each component (React + Flask + PostgreSQL) and run everything with Docker Compose.

---

## Project Structure
```
three-tier-docker/
├── backend/
│   ├── app.py
│   ├── requirements.txt
│   └── Dockerfile
├── frontend/
│   ├── src/App.jsx
│   ├── package.json   (created by Vite)
│   └── Dockerfile
├── database/
│   └── init.sql
└── docker-compose.yml
```

---

## Step 1: Create Folders
```bash
cd %USERPROFILE%\Desktop
mkdir three-tier-docker
cd three-tier-docker
mkdir backend frontend database
```

---

## Step 2: Backend

### `backend/app.py`
```python
from flask import Flask, jsonify
import psycopg2
import os

app = Flask(__name__)

@app.route("/")
def home():
    return "Flask Backend is Running"

@app.route("/students")
def students():
    try:
        conn = psycopg2.connect(
            host=os.getenv("DB_HOST"),
            database=os.getenv("DB_NAME"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD")
        )
        cur = conn.cursor()
        cur.execute("SELECT id, name, email, course FROM students ORDER BY id")
        rows = cur.fetchall()
        cur.close()
        conn.close()

        result = []
        for row in rows:
            result.append({
                "id": row[0],
                "name": row[1],
                "email": row[2],
                "course": row[3]
            })
        return jsonify(result)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
```

### `backend/requirements.txt`
```
Flask
psycopg2-binary
flask-cors
```

### `backend/Dockerfile`
```dockerfile
FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["python", "app.py"]
```

---

## Step 3: Frontend

```bash
cd frontend
npm create vite@latest . -- --template react
# type y when asked
npm install
npm install axios
```

### Replace `src/App.jsx`
(See `frontend/src/App.jsx` in this folder)

### `frontend/Dockerfile`
```dockerfile
FROM node:20

WORKDIR /app

COPY package*.json ./
RUN npm install

COPY . .

EXPOSE 5173

CMD ["npm", "run", "dev", "--", "--host", "0.0.0.0"]
```

---

## Step 4: Database

### `database/init.sql`
```sql
CREATE TABLE IF NOT EXISTS students (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL,
    course VARCHAR(100) NOT NULL
);

INSERT INTO students (name, email, course)
VALUES
('Rahul', 'rahul@gmail.com', 'BCA'),
('Priya', 'priya@gmail.com', 'BSc CS'),
('Amit', 'amit@gmail.com', 'BCA');
```

---

## Step 5: docker-compose.yml (root folder)
```yaml
services:
  frontend:
    build: ./frontend
    container_name: student_frontend
    ports:
      - "5173:5173"
    depends_on:
      - backend

  backend:
    build: ./backend
    container_name: student_backend
    ports:
      - "5000:5000"
    environment:
      DB_HOST: database
      DB_NAME: studentdb
      DB_USER: postgres
      DB_PASSWORD: postgres
    depends_on:
      - database

  database:
    image: postgres:16
    container_name: student_database
    restart: always
    environment:
      POSTGRES_DB: studentdb
      POSTGRES_USER: postgres
      POSTGRES_PASSWORD: postgres
    ports:
      - "5432:5432"
    volumes:
      - postgres_data:/var/lib/postgresql/data
      - ./database/init.sql:/docker-entrypoint-initdb.d/init.sql

volumes:
  postgres_data:
```

> Inside Docker, Flask connects to host **`database`** (service name), not `localhost`.

---

## Step 6: Build & Run

```bash
cd three-tier-docker
docker compose build
docker compose up -d
```

### Check status
```bash
docker compose ps
docker ps
```

### Open application
http://localhost:5173

You should see the Student Management System with 3 students.

### View logs
```bash
docker compose logs frontend
docker compose logs backend
docker compose logs database
```

### Stop
```bash
docker compose down
```

### Restart later
```bash
docker compose up -d
```

---

## Commands Summary

| Command                         | Purpose |
|---------------------------------|---------|
| `docker compose build`          | Build images |
| `docker compose up -d`          | Start all services |
| `docker compose ps`             | Status |
| `docker compose logs <service>` | View logs |
| `docker compose down`           | Stop & remove containers |

---

## Final Architecture
```
Browser
   │
   ▼
React Frontend (:5173)  ──►  Flask Backend (:5000)  ──►  PostgreSQL (:5432)
   container                      container                   container
```
