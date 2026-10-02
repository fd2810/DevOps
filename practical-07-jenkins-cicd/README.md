# Practical 7: Setting Up CI/CD with Jenkins

## Aim
Set up Jenkins for a Flask application and create a CI/CD pipeline that does:
**Developer → GitHub → Jenkins → Build → Test → Deploy**

---

## What You Need Installed

| Software       | Purpose |
|----------------|---------|
| JDK 17+        | Required by Jenkins |
| Jenkins        | CI/CD automation |
| Git            | Version control |
| Python + Flask | Application |
| pytest         | Automated testing |
| GitHub account | Remote repository |

---

## Part A — Install Jenkins

### 1. Check Java
```bash
java -version
```

### 2. Check Git
```bash
git --version
```

### 3. Install Jenkins
- Download Windows installer from https://www.jenkins.io/download/
- Run the installer
- Keep default port **8080**
- Complete installation

### 4. Open Jenkins
Browser → http://localhost:8080

Unlock Jenkins using the initial admin password (shown during install or in:
`C:\Program Files\Jenkins\secrets\initialAdminPassword`)

Install suggested plugins → Create admin user.

---

## Part B — Create a Simple Flask Project

### Project structure
```
Flask-CI-CD/
├── app.py
├── test_app.py
├── requirements.txt
└── Jenkinsfile
```

### `app.py`
```python
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello from Flask CI/CD!"

@app.route("/hello")
def hello():
    return "Hello from Jenkins!"

if __name__ == "__main__":
    app.run(debug=True)
```

### `test_app.py`
```python
from app import app

def test_home():
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200
    assert b"Hello from Flask CI/CD!" in response.data
```

### `requirements.txt`
```
Flask
pytest
```

### `Jenkinsfile` (Declarative Pipeline)
```groovy
pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        stage('Install Dependencies') {
            steps {
                bat 'python -m pip install -r requirements.txt'
            }
        }
        stage('Test') {
            steps {
                bat 'python -m pytest test_app.py -v'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deployment stage (can start the app or copy files)'
            }
        }
    }
}
```

> On Linux agents use `sh` instead of `bat`.

---

## Part D — Test the Application Manually
Open the VS Code terminal.
1. Create a virtual environment:
    python -m venv venv
2. Activate it:
    venv\Scripts\activate
3. Install dependencies:
    pip install -r requirements.txt
4. Run the test:
    pytest
5. You should get:
    1 passed
6. Run Flask:
    python app.py
7. Open: http://localhost:5000
8. You should see:
    Hello from Flask CI/CD!
---

## Part D — Push Project to GitHub

```bash
git init
git add .
git commit -m "Initial Flask CI/CD project"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/Flask-CI-CD.git
git push -u origin main
```

---

## Part E — Create Jenkins Pipeline Job

1. Jenkins Dashboard → **New Item**
2. Name: `Flask-CI-CD`
3. Select **Pipeline** → OK
4. Under **Pipeline**:
   - Definition: **Pipeline script from SCM**
   - SCM: **Git**
   - Repository URL: your GitHub repo URL
   - Branch: `*/main`
   - Script Path: `Jenkinsfile`
5. Save

---

## Part F — Run the Pipeline

Click **Build Now**.

Watch **Console Output**:
- Checkout
- Install dependencies
- Tests (should show `1 passed`)
- Finished: **SUCCESS**

---

## Part G — (Optional) GitHub Webhook for Automatic Trigger

1. In Jenkins job → Configure → Build Triggers → check **GitHub hook trigger for GITScm polling**
2. In GitHub repo → Settings → Webhooks → Add webhook  
   Payload URL: `http://YOUR_JENKINS_SERVER/github-webhook/`  
   Content type: `application/json`  
   Events: Just the push event

> Note: If Jenkins is on `localhost`, GitHub cannot reach it. For classroom demo, use **Build Now**. For real auto-trigger, Jenkins needs a public URL (or ngrok/tunnel).

---

## What to Show Teacher
1. `java -version` and `git --version`
2. Jenkins dashboard (http://localhost:8080)
3. GitHub repository
4. Pipeline configuration
5. Console Output showing **SUCCESS** and tests passed
6. (Optional) Make a code change → `git push` → new build appears
