#!/bin/sh
set -eu
PROJECT_DIR=$(CDPATH= cd -- "$(dirname -- "$0")/.." && pwd)
RENPY_SDK=${RENPY_SDK:-/Users/limit/Tools/renpy-8.5.3-sdk}
cd "$PROJECT_DIR"
mkdir -p artifacts
python3 tools/check_assets.py > artifacts/assets.txt
python3 -m unittest discover -s tests -v > artifacts/import-tests.txt 2>&1
"$RENPY_SDK/renpy.sh" "$PROJECT_DIR" lint > artifacts/lint.txt 2>&1
# Some lint diagnostics do not result in a non-zero process status.
python3 tools/check_lint.py artifacts/lint.txt
"$RENPY_SDK/renpy.sh" "$PROJECT_DIR" --savedir "$PROJECT_DIR/artifacts/test-saves" test demo --report-detailed --overwrite-screenshots > artifacts/engine-tests.txt 2>&1
python3 -c 'from pathlib import Path; s=Path("artifacts/engine-tests.txt").read_text(); assert "Status: PASSED" in s, s'
echo 'PASS: assets, photo importer, Ren’Py lint, engine UI/branch/save/load tests.'
