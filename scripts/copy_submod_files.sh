#!/usr/bin/env bash
set -euo pipefail

# Usage:
#   ./copy-diff.sh <branch1> <branch2> <destination_dir>
#
# Example:
#   ./copy-diff.sh feature-x feature-y B

BRANCH1=${1:-}
BRANCH2=${2:-}
DEST_DIR=${3:-}

if [[ -z "$BRANCH1" || -z "$BRANCH2" || -z "$DEST_DIR" ]]; then
  echo "Usage: $0 <branch1> <branch2> <destination_dir>"
  exit 1
fi

SOURCE_DIRS=("deploy")

echo "Comparing $BRANCH1 and $BRANCH2..."
echo "Copying differing files from ${SOURCE_DIRS[*]} into $DEST_DIR/"

for SRC_DIR in "${SOURCE_DIRS[@]}"; do
  echo "Checking directory: $SRC_DIR"

  # Get differing files in this source directory
  mapfile -t files < <(git diff --name-only "$BRANCH1" "$BRANCH2" -- "$SRC_DIR")

  for f in "${files[@]}"; do
    # Safety: ensure the file actually belongs to SRC_DIR
    if [[ "$f" != "$SRC_DIR"* ]]; then
      continue
    fi

    # Strip the SRC_DIR prefix so that folder itself is not copied
    rel_path="${f#$SRC_DIR/}"
    target="$DEST_DIR/$rel_path"

    mkdir -p "$(dirname "$target")"

    # Copy only if the file exists in BRANCH2
    if git cat-file -e "$BRANCH2:$f" 2>/dev/null; then
      git show "$BRANCH2:$f" > "$target"
      echo "Copied: $f → $target"
    else
      echo "⚠️ Skipped (deleted in $BRANCH2): $f"
    fi
  done
done

echo
echo "✅ Done!"