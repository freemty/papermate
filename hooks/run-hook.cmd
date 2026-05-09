#!/bin/bash
# Dispatcher for papermate hooks
# Usage: run-hook.cmd <hook-name>

HOOK_NAME="$1"
HOOK_DIR="$(cd "$(dirname "$0")" && pwd)"
HOOK_PATH="${HOOK_DIR}/${HOOK_NAME}"

if [ ! -f "$HOOK_PATH" ]; then
  exit 0
fi

if [ ! -x "$HOOK_PATH" ]; then
  chmod +x "$HOOK_PATH"
fi

exec "$HOOK_PATH"
