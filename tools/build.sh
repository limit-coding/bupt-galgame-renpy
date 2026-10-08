#!/bin/sh
set -eu
PROJECT_DIR=$(CDPATH= cd -- "$(dirname -- "$0")/.." && pwd)
RENPY_SDK=${RENPY_SDK:-/Users/limit/Tools/renpy-8.5.3-sdk}
DESTINATION=${1:-"$PROJECT_DIR/../renpy-releases"}
"$RENPY_SDK/renpy.sh" "$RENPY_SDK/launcher" distribute "$PROJECT_DIR" --destination "$DESTINATION" --package win --package mac --no-update
