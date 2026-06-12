#!/bin/bash
# Create the project-local Python 3.10 environment used by Hypium.

set -euo pipefail

PROJECT_DIR="$(cd "$(dirname "$0")/.." && pwd)"
VENV_DIR="$PROJECT_DIR/.venv-hypium"
PYTHON_BIN="${PYTHON310:-}"

if [[ -z "$PYTHON_BIN" ]]; then
    for candidate in python3.10 /opt/homebrew/bin/python3.10 /usr/local/bin/python3.10; do
        if command -v "$candidate" >/dev/null 2>&1; then
            PYTHON_BIN="$(command -v "$candidate")"
            break
        fi
    done
fi

if [[ -z "$PYTHON_BIN" ]]; then
    echo "错误: 未找到 Python 3.10。"
    echo "macOS 可运行: brew install python@3.10"
    exit 1
fi

"$PYTHON_BIN" -m venv "$VENV_DIR"
"$VENV_DIR/bin/python" -m pip install -U pip
"$VENV_DIR/bin/pip" install \
    -r "$PROJECT_DIR/hypium/requirements.txt" \
    --trusted-host mirrors.huaweicloud.com \
    -i https://mirrors.huaweicloud.com/repository/pypi/simple

"$VENV_DIR/bin/python" - <<'PY'
import hypium
from PIL import Image

print("Hypium:", hypium.__version__)
print("Pillow:", Image.__version__)
PY
