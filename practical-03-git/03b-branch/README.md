# Practical 3b: Git Branching and Merging

## Aim
Create a new branch, make changes, and merge it back into main.

## Prerequisites
You already have a Git repository from Practical 3a (`Git_Practical` folder with `hello.py`).

---

## Step-by-Step

### 1. Check current branch
```bash
git branch
```

### 2. Create and switch to a new branch
```bash
git checkout -b feature-branch
```

or (newer Git):
```bash
git switch -c feature-branch
```

### 3. Modify `hello.py`
Change content to:
```python
print("Hello Git!")
print("This is feature branch")
```

### 4. Stage and commit on feature branch
```bash
git add hello.py
git commit -m "Added feature branch message"
```

### 5. Switch back to main
```bash
git checkout main
```

### 6. Merge feature branch into main
```bash
git merge feature-branch
```

### 7. Verify
```bash
git log --oneline
git branch
```

### 8. (Optional) Delete feature branch after merge
```bash
git branch -d feature-branch
```

---

## Commands Summary

| Command | Purpose |
|---------|---------|
| `git branch` | List branches |
| `git checkout -b <name>` | Create + switch to new branch |
| `git switch -c <name>` | Same (modern) |
| `git merge <branch>` | Merge branch into current |
| `git branch -d <name>` | Delete branch |
