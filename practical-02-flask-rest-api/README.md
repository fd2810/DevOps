# Practical 2: Building a REST API with Flask

## Aim
- Create a simple REST API using Flask with **CRUD operations** for a To-Do List application.
- Test the API using **curl** or Postman.

---

## Prerequisites
- Python 3 installed
- Command Prompt / PowerShell / Terminal

---

## Step 1: Check Python

```bash
python --version
```

Expected output (example):
```
Python 3.12.4
```

---

## Step 2: Create Project Folder

```bash
mkdir Flask_Project
cd Flask_Project
```

---

## Step 3: Create & Activate Virtual Environment

```bash
python -m venv venv
```

**Windows:**
```bash
venv\Scripts\activate
```

**Linux / Mac:**
```bash
source venv/bin/activate
```

You should see `(venv)` in the terminal.

---

## Step 4: Install Flask

```bash
pip install flask
```

Verify:
```bash
pip show flask
```

---

## Step 5: Code 1 – Simple Hello Flask App

Create file: `app_hello.py`

```python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, Flask!"

if __name__ == '__main__':
    app.run(debug=True)
```

### Run
```bash
python app_hello.py
```

Open browser: http://127.0.0.1:5000  
Output: `Hello, Flask!`

---

## Step 6: Code 2 – JSON Response

Create file: `app_json.py`

```python
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({
        "message": "Welcome to my first Flask API",
        "status": "success"
    })

if __name__ == '__main__':
    app.run(debug=True)
```

### Run
```bash
python app_json.py
```

Open: http://127.0.0.1:5000  
You will get JSON response.

---

## Step 7: Code 3 – Full CRUD To-Do API (Main Code)

Create file: `app.py` (or `app_crud.py`)

```python
from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample data storage (in-memory)
todos = [
    {
        "id": 1,
        "title": "Learn Flask",
        "completed": False
    }
]

# CREATE a new task
@app.route('/todos', methods=['POST'])
def create_todo():
    data = request.get_json()
    new_todo = {
        "id": len(todos) + 1,
        "title": data['title'],
        "completed": False
    }
    todos.append(new_todo)
    return jsonify(new_todo), 201

# READ all tasks
@app.route('/todos', methods=['GET'])
def get_todos():
    return jsonify(todos)

# READ a single task
@app.route('/todos/<int:id>', methods=['GET'])
def get_todo(id):
    todo = next((t for t in todos if t['id'] == id), None)
    if todo is None:
        return jsonify({"message": "Task not found"}), 404
    return jsonify(todo)

# UPDATE a task
@app.route('/todos/<int:id>', methods=['PUT'])
def update_todo(id):
    todo = next((t for t in todos if t['id'] == id), None)
    if todo is None:
        return jsonify({"message": "Task not found"}), 404
    data = request.get_json()
    todo['title'] = data.get('title', todo['title'])
    todo['completed'] = data.get('completed', todo['completed'])
    return jsonify(todo)

# DELETE a task
@app.route('/todos/<int:id>', methods=['DELETE'])
def delete_todo(id):
    global todos
    todo = next((t for t in todos if t['id'] == id), None)
    if todo is None:
        return jsonify({"message": "Task not found"}), 404
    todos = [t for t in todos if t['id'] != id]
    return jsonify({"message": "Task deleted successfully"})

if __name__ == '__main__':
    app.run(debug=True)
```

### Run the CRUD API
```bash
python app.py
```

---

## Step 8: Test with curl

### 1. GET all tasks
```bash
curl http://127.0.0.1:5000/todos
```

### 2. POST (Create new task)
```bash
curl -X POST http://127.0.0.1:5000/todos -H "Content-Type: application/json" -d "{\"title\":\"Complete REST API Assignment\"}"
```

### 3. GET single task
```bash
curl http://127.0.0.1:5000/todos/1
```

### 4. PUT (Update task)
```bash
curl -X PUT http://127.0.0.1:5000/todos/1 -H "Content-Type: application/json" -d "{\"title\":\"Learn Flask API\",\"completed\":true}"
```

### 5. DELETE task
```bash
curl -X DELETE http://127.0.0.1:5000/todos/1
```

### 6. Verify deletion
```bash
curl http://127.0.0.1:5000/todos
```

---

## Quick Reference (Viva)

| HTTP Method | Endpoint     | Purpose                  |
|-------------|--------------|--------------------------|
| GET         | /todos       | Get all tasks            |
| GET         | /todos/1     | Get one task             |
| POST        | /todos       | Create new task          |
| PUT         | /todos/1     | Update existing task     |
| DELETE      | /todos/1     | Delete a task            |

---

## Files in this folder
- `app_hello.py` – Code 1
- `app_json.py`  – Code 2
- `app.py`       – Code 3 (Full CRUD)
