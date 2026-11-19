#!/usr/bin/env bash
set -eu
# Do not install a guessed verifier version, even on a trusted runner.
echo 'BLOCKED: competition-compatible tool revisions are not pinned. See docs/competition_contract.md.' >&2
exit 1
