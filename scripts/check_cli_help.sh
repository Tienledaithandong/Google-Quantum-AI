#!/usr/bin/env bash
# Offline parser checks. Never pass a competition name or issue a request.
set -euo pipefail
kaggle --version
files=$(kaggle competitions files --help)
download=$(kaggle competitions download --help)
printf '%s\n' "$files" "$download"
grep -Fq -- '--page-size' <<<"$files"
grep -Fq -- '--file' <<<"$download"
grep -Fq -- '--path' <<<"$download"
