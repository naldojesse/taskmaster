#!/bin/bash

# Configuration
PRIVATE_REPO="."
PUBLIC_REPO="../taskmaster-public"
PUBLIC_REMOTE="public"  # Changed back to "public" to match your remote setup

# Ensure the public repo directory exists
mkdir -p "$PUBLIC_REPO"

# Sync files from private to public repo, excluding sensitive information
rsync -av --delete \
    --exclude='.git/' \
    --exclude='docs/*' \
    --include='docs/public/' \
    --exclude='*.env' \
    --exclude='node_modules/' \
    --exclude='build/' \
    --exclude='*.log' \
    --exclude='*.bak' \
    "$PRIVATE_REPO/" "$PUBLIC_REPO/"

# Copy public-specific files
cp "$PRIVATE_REPO/config/public/README.md" "$PUBLIC_REPO/README.md"
cp "$PRIVATE_REPO/config/public/.gitignore" "$PUBLIC_REPO/.gitignore"
cp "$PRIVATE_REPO/config/public/LICENSE" "$PUBLIC_REPO/LICENSE"
cp "$PRIVATE_REPO/config/public/CONTRIBUTING.md" "$PUBLIC_REPO/CONTRIBUTING.md"

# Change to the public repo directory
cd "$PUBLIC_REPO" || exit 1

# Initialize git if not already initialized
if [ ! -d .git ]; then
    git init
    git remote add public https://github.com/naldojesse/taskmaster.git
else
    # Ensure the remote is set correctly
    git remote set-url public https://github.com/naldojesse/taskmaster.git
fi

# Add all changes
git add .

# Commit changes if there are any
if git diff --staged --quiet; then
    echo "No changes to commit"
else
    git commit -m "Sync from private repo"
fi

# Push changes to the public remote
git push -u public main

# Return to the private repo directory
cd "$PRIVATE_REPO" || exit 1

echo "Sync completed successfully"