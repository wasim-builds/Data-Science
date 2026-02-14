# 🤖 Git & GitHub Cheat Sheet

## 🚀 Setup
```bash
git init                   # Start repo
git clone <url>            # Copy repo
git config user.name "Name"
git config user.email "email"
```

## 💾 Saving Changes
```bash
git status                 # Check changes
git add .                  # Stage all
git commit -m "Message"    # Save
```

## 🔄 Syncing
```bash
git pull origin main       # Get updates
git push origin main       # Send updates
```

## 🌿 Branching
```bash
git branch                 # List branches
git checkout -b new-feat   # Create & switch
git checkout main          # Switch back
git merge new-feat         # Combine
```

## 🔙 Undo
```bash
git reset --soft HEAD~1    # Undo commit, keep changes
git checkout .             # Aaaah! Revert file changes
```
