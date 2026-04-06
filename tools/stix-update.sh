#!/bin/bash
# STIX Update Checker — Check if your version is current
CURRENT_VERSION=$(grep -o 'V[0-9]*\.[0-9]*' CLAUDE.md | head -1)
REMOTE_VERSION=$(curl -s https://raw.githubusercontent.com/0Gizmick0/stix-v1/main/CLAUDE.md \
  | grep -o 'V[0-9]*\.[0-9]*' | head -1)

if [ "$CURRENT_VERSION" = "$REMOTE_VERSION" ]; then
  echo "✅ STIX is current ($CURRENT_VERSION)"
else
  echo "⚠️  Update available: $CURRENT_VERSION → $REMOTE_VERSION"
  echo "Run: git pull origin main"
fi
