#!/bin/zsh
set -eu
PROJECT_DIR="$(cd "$(dirname "$0")" && pwd)"
RENPY_SDK="${RENPY_SDK:-/Users/limit/Tools/renpy-8.5.3-sdk}"
if [[ ! -x "$RENPY_SDK/renpy.sh" ]]; then
  echo "未找到 Ren'Py SDK。请从 https://www.renpy.org/latest.html 下载 8.5.3 或更新稳定版，使用启动器打开本工程。"
  echo "也可以设置 RENPY_SDK 为解压后的 SDK 路径。"
  read -r "?按回车关闭。"
  exit 1
fi
exec "$RENPY_SDK/renpy.sh" "$PROJECT_DIR"
