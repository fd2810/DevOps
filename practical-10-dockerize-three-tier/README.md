# Practical 10: Dockerize 3-Tier Application with Docker Compose

## Aim
Dockerize each component (React + Flask + PostgreSQL) and run everything with **Docker Compose**.

---

## Project Structure
```
three-tier-docker/          (or practical-10-dockerize-three-tier/)
├── backend/
│   ├── app.py
│   ├── requirements.txt
│   └── Dockerfile
├── frontend/
│   ├── src/App.jsx
│   ├── src/main.jsx
│   ├── package.json
│   ├── index.html
│   ├── vite.config.js
│   └── Dockerfile
├── database/
│   └── init.sql
└── docker-compose.yml
```

---

## Important Notes (to avoid errors)

1. **Backend connects using container name**  
   In `backend/app.py`:
   ```python
   host="student_database"   # must match container_name of database
   password="123456"         # must match POSTGRES_PASSWORD
   ```

2. **API path**  
   - Backend route: `/api/students`  
   - Frontend calls: `http://localhost:5000/api/students`

3. **CORS** is enabled in backend so React can talk to Flask.

4. **Password** used everywhere: `123456`

---

## Step 1: Create Folders
```bash
cd %USERPROFILE%\Desktop
mkdir three-tier-docker
cd three-tier-docker
mkdir backend frontend database
```

Copy all files from this practical folder into the matching places.

---

## Step 2: Backend files (already provided)

- `backend/app.py`
- `backend/requirements.txt`
- `backend/Dockerfile`

---

## Step 3: Frontend

If you start from scratch:
```bash
cd frontend
npm create vite@latest . -- --template react
# type y when asked
npm install
```

Then **replace** `src/App.jsx` and `src/main.jsx` with the files from this folder.  
Also copy `Dockerfile`, `index.html`, `package.json`, `vite.config.js`.

---

## Step 4: Database

`database/init.sql` creates the table and inserts sample students.

---

## Step 5: docker-compose.yml

Already provided in the root of this folder.

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
**http://localhost:5173**

You should see the Student Management table with:
| ID | Name  | Email             | Course  |
|----|-------|-------------------|---------|
| 1  | Rahul | rahul@gmail.com   | BCA     |
| 2  | Priya | priya@gmail.com   | BSc CS  |
| 3  | Amit  | amit@gmail.com    | BCA     |

### View logs (if something fails)
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

| Command | Purpose |
|---------|---------|
| `docker compose build` | Build images |
| `docker compose up -d` | Start all services |
| `docker compose ps` | Status |
| `docker compose logs <service>` | View logs |
| `docker compose down` | Stop & remove containers |

---

## Final Architecture
```
Browser
   │
   ▼
React Frontend (:5173)  ──►  Flask Backend (:5000)  ──►  PostgreSQL (:5432)
   container                      container                   container
                              /api/students              student_database
```
