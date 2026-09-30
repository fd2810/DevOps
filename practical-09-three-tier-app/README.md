# Practical 9: 3-Tier Architecture (React + Flask + PostgreSQL)

## Aim
Build a Student Management System with three tiers:

| Tier | Technology | Port |
|------|------------|------|
| Frontend (Presentation) | React (Vite) | 5173 |
| Backend (Application) | Flask | 5000 |
| Database (Data) | PostgreSQL | 5433 (or 5432) |

---

## Architecture
```
React Frontend  ──HTTP──►  Flask Backend  ──SQL──►  PostgreSQL
   :5173                      :5000                    :5433
```

---

## Step 1: Check Installed Tools
```bash
python --version
node --version
npm --version
```

PostgreSQL (adjust path if needed):
```bash
"C:\Program Files\PostgreSQL\18\bin\psql.exe" --version
```

---

## Step 2: Create Project Folders
```bash
cd %USERPROFILE%\Desktop
mkdir three-tier-student-app
cd three-tier-student-app
mkdir backend
mkdir frontend
```

---

## Step 3: Create PostgreSQL Database

1. Open **pgAdmin**
2. Servers → PostgreSQL → Databases → Create → Database
3. Name: `studentdb2` → Save

### Create table (Query Tool)
```sql
CREATE TABLE students (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL,
    course VARCHAR(100) NOT NULL
);
```

### Insert sample data
```sql
INSERT INTO students (name, email, course)
VALUES
('Rahul', 'rahul@gmail.com', 'BCA'),
('Priya', 'priya@gmail.com', 'BSc CS'),
('Amit', 'amit@gmail.com', 'BCA');
```

---

## Step 4: Flask Backend

```bash
cd backend
python -m venv venv
venv\Scripts\activate
pip install flask flask-cors "psycopg[binary]"
```

### Create `app.py`
(See `backend/app.py` in this folder)

**Important:** Change the password in `DB_CONFIG` to your real PostgreSQL password.

### Run backend
```bash
python app.py
```

Test:
- http://127.0.0.1:5000/ → `{"message": "Student Management API is running"}`
- http://127.0.0.1:5000/students → list of students

---

## Step 5: React Frontend

Open **new** terminal:
```bash
cd %USERPROFILE%\Desktop\three-tier-student-app
npm create vite@latest frontend -- --template react
cd frontend
npm install
npm install axios
```

### Replace `src/App.jsx`
(See `frontend/src/App.jsx`)

### Replace `src/App.css`
(See `frontend/src/App.css`)

### Run frontend
```bash
npm run dev
```

Open the URL shown (usually http://localhost:5173)

You should see the Student Management System table with data coming from PostgreSQL via Flask.

---

## Expected Result
Data flows:  
**React → Flask API → PostgreSQL → Flask → React**

Students are **not hard-coded** in React.
