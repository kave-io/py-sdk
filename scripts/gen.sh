#!/usr/bin/env bash
# Regenerate gRPC stubs from proto files.
# Run from kave-py root: ./scripts/gen.sh
set -euo pipefail

REPO_ROOT="$(cd "$(dirname "$0")/../.." && pwd)"
PROTO_ROOT="$REPO_ROOT/core/proto"
OUT_DIR="$(cd "$(dirname "$0")/.." && pwd)/kave"
GRPC_TOOLS_DIR=$(uv run python -m grpc_tools --print-path 2>/dev/null || uv run python -c "import grpc_tools, os; print(os.path.dirname(grpc_tools.__file__))")

echo "proto root: $PROTO_ROOT"
echo "output:     $OUT_DIR"

# Remove old generated files (keep our package files)
find "$OUT_DIR" -name "*_pb2*.py" -o -name "*_pb2*.pyi" | xargs rm -f

uv run python -m grpc_tools.protoc \
  -I"$PROTO_ROOT" \
  -I"$GRPC_TOOLS_DIR" \
  --python_out="$OUT_DIR" \
  --pyi_out="$OUT_DIR" \
  --grpc_python_out="$OUT_DIR" \
  $(find "$PROTO_ROOT" -name "*.proto")

# Ensure __init__.py exists in all generated subdirs
find "$OUT_DIR" -type d | while read -r d; do
  [ -f "$d/__init__.py" ] || touch "$d/__init__.py"
done

echo "done"
