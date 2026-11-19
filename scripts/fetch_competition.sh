#!/usr/bin/env bash
set -eu
if [[ ${GITHUB_EVENT_NAME:-} != workflow_dispatch || ${GITHUB_REF:-} != refs/heads/main ]]; then
  echo 'BLOCKED: download requires an approved manual workflow on protected main.' >&2
elif [[ -z ${KAGGLE_API_TOKEN:-} ]]; then
  echo 'HUMAN_ACTION_REQUIRED: configure the protected benchmark environment (issue #2).' >&2
else
  echo 'BLOCKED: rules, CLI version and official asset paths require audit (issue #1).' >&2
fi
exit 1
