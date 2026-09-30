# Practical 3c: Creating and Resolving Merge Conflict

## Aim
Intentionally create a merge conflict and resolve it.

## Prerequisites
Git repository with `hello.py` on main branch.

---

## Step-by-Step

### 1. Make sure you are on main
```bash
git checkout main
```

### 2. Create a new branch
```bash
git checkout -b feature-conflict
```

### 3. Edit `hello.py` on feature-conflict branch
```python
print("Hello Git!")
print("Feature Branch Version")
```

### 4. Commit on feature branch
```bash
git add hello.py
git commit -m "Modified hello.py in feature branch"
```

### 5. Switch to main
```bash
git checkout main
```

### 6. Edit `hello.py` on main (different change)
```python
print("Hello Git!")
print("Main Branch Version")
```

### 7. Commit on main
```bash
git add hello.py
git commit -m "Modified hello.py in main branch"
```

### 8. Attempt to merge (this will cause conflict)
```bash
git merge feature-conflict
```

You will see conflict markers in `hello.py`:
```
<<<<<<< HEAD
print("Main Branch Version")
=======
print("Feature Branch Version")
>>>>>>> feature-conflict
```

### 9. Resolve the conflict
Open `hello.py` and edit it to final desired version, for example:
```python
print("Hello Git!")
print("Main Branch Version")
print("Feature Branch Version")
```

Remove all conflict markers (`<<<<<<<`, `=======`, `>>>>>>>`).

### 10. Stage the resolved file
```bash
git add hello.py
```

### 11. Complete the merge
```bash
git commit -m "Resolved merge conflict"
```

### 12. Verify
```bash
git log --oneline
git status
```

Status should show: `nothing to commit, working tree clean`

---

## Final `hello.py` (after resolution)
```python
print("Hello Git!")
print("Main Branch Version")
print("Feature Branch Version")
```

---

## Viva Questions

**Q1. What is a merge conflict?**  
When Git cannot automatically merge changes because the same lines were modified differently in two branches.

**Q2. How do you resolve it?**  
Edit the file, remove conflict markers, keep the correct code, then `git add` + `git commit`.

**Q3. What are conflict markers?**  
`<<<<<<<`, `=======`, `>>>>>>>`
