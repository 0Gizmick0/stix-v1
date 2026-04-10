#!/usr/bin/env bash
# STIX Setup — Create project structure for Claude Code / IDE users
# Usage: bash tools/stix-setup.sh [project-name]
# Idempotent: safe to run multiple times.
set -euo pipefail

REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
PROJECT_NAME="${1:-my-first-project}"

# Validate project name
if [[ ! "$PROJECT_NAME" =~ ^[a-zA-Z0-9_-]+$ ]]; then
  echo "Error: project name must be alphanumeric (hyphens and underscores OK)."
  echo "Usage: bash tools/stix-setup.sh my-project-name"
  exit 1
fi

PROJECT_DIR="$REPO_ROOT/projects/$PROJECT_NAME"

# 1. Create project directory
mkdir -p "$PROJECT_DIR"

# 2. Copy about.md from template (if not already present)
if [ ! -f "$PROJECT_DIR/about.md" ]; then
  cp "$REPO_ROOT/templates/about_template.md" "$PROJECT_DIR/about.md"
  sed -i.bak "s/\[Project Name\]/$PROJECT_NAME/g" "$PROJECT_DIR/about.md"
  sed -i.bak "s/\[YYYY-MM-DD\]/$(date +%Y-%m-%d)/g" "$PROJECT_DIR/about.md"
  rm -f "$PROJECT_DIR/about.md.bak"
  echo "  Created: projects/$PROJECT_NAME/about.md"
else
  echo "  Exists:  projects/$PROJECT_NAME/about.md (skipped)"
fi

# 3. Copy audit_log.md from template (if not already present)
if [ ! -f "$PROJECT_DIR/audit_log.md" ]; then
  cp "$REPO_ROOT/templates/audit_log_template.md" "$PROJECT_DIR/audit_log.md"
  sed -i.bak "s/\[Project Name\]/$PROJECT_NAME/g" "$PROJECT_DIR/audit_log.md"
  sed -i.bak "s/\[project name\]/$PROJECT_NAME/g" "$PROJECT_DIR/audit_log.md"
  sed -i.bak "s/\[YYYY-MM-DD\]/$(date +%Y-%m-%d)/g" "$PROJECT_DIR/audit_log.md"
  rm -f "$PROJECT_DIR/audit_log.md.bak"
  echo "  Created: projects/$PROJECT_NAME/audit_log.md"
else
  echo "  Exists:  projects/$PROJECT_NAME/audit_log.md (skipped)"
fi

# 4. Create session_state directory with stub
SESSION_DIR="$REPO_ROOT/session_state"
mkdir -p "$SESSION_DIR"
if [ ! -f "$SESSION_DIR/current.md" ]; then
  cat > "$SESSION_DIR/current.md" << EOF
# Session State — Current
Initialized: $(date +%Y-%m-%d)
Active project: $PROJECT_NAME
EOF
  echo "  Created: session_state/current.md"
else
  echo "  Exists:  session_state/current.md (skipped)"
fi

# 5. Ensure projects/ and session_state/ are gitignored
if ! grep -q '^projects/' "$REPO_ROOT/.gitignore" 2>/dev/null; then
  printf '\n# User project data (created by stix-setup.sh)\nprojects/\nsession_state/\n' >> "$REPO_ROOT/.gitignore"
  echo "  Updated: .gitignore"
fi

echo ""
echo "STIX setup complete."
echo "  Project:  projects/$PROJECT_NAME/"
echo "  Files:    about.md, audit_log.md"
echo "  State:    session_state/current.md"
echo ""
echo "Next: open this directory in Claude Code and start a session."
