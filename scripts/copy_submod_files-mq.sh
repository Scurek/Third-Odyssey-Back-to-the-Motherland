#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

BRANCH1="development"
BRANCH2="Land-of-Muhammad-Qu-compatibility"
DEST_DIR="submods/TO_MQ_compatibility"

# Call the main script
"$SCRIPT_DIR/copy_submod_files.sh" "$BRANCH1" "$BRANCH2" "$DEST_DIR"