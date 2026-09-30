# Practical 3a: Git Repository Initialization

## Aim
Create a Git repository, initialize it, and add a simple Python project.

## Software Required
- Git
- Visual Studio Code (or any editor)
- Python

---

## Step-by-Step

### 1. Open Terminal in VS Code
`Terminal → New Terminal`

### 2. Go to Desktop
```bash
cd Desktop
```

### 3. Create project folder
```bash
mkdir Git_Practical
cd Git_Practical
```

### 4. Open folder in VS Code
```bash
code .
```

### 5. Create `hello.py`
```python
print("Hello Git!")
```

### 6. Create `README.md`
```markdown
# Git Practical
This is my first Git repository.
Project Name: Python Demo
Created by: Your Name
```

### 7. Initialize Git
```bash
git init
```

Expected output:
```
Initialized empty Git repository in .../Git_Practical/.git/
```

### 8. Check status
```bash
git status
```

You will see untracked files: `hello.py` and `README.md`

### 9. Add files
```bash
git add .
```

### 10. Configure Git (first time only)
```bash
git config --global user.name "Your Name"
git config --global user.email "your@email.com"
```

### 11. Commit
```bash
git commit -m "Initial commit - added hello.py and README"
```

### 12. Check log
```bash
git log --oneline
```

### 13. (Optional) Connect to GitHub
```bash
git remote add origin https://github.com/YOUR_USERNAME/Git_Practical.git
git branch -M main
git push -u origin main
```

---

## Commands Summary

| Step | Command | Purpose |
|------|---------|---------|
| 1 | `git init` | Create repository |
| 2 | `git status` | See current state |
| 3 | `git add .` | Stage all files |
| 4 | `git commit -m "message"` | Save snapshot |
| 5 | `git log --oneline` | View history |
