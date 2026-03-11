#!/bin/bash
# Get script file dir
script_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

uv tool uninstall auraview
uv tool install "$script_dir"
