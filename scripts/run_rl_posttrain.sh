#!/usr/bin/env bash
# RL post-training entry point.
#
# TODO: wire this up to the actual training framework used in the paper
# (e.g. verl / OpenRLHF / TRL). For now this is just a placeholder.

set -euo pipefail

DATA=${DATA:-data/filtered/train.vidground.jsonl}
OUTPUT_DIR=${OUTPUT_DIR:-checkpoints/vidground-rl}

echo "[vidground] data:        ${DATA}"
echo "[vidground] output dir:  ${OUTPUT_DIR}"
echo "[vidground] TODO: launch RL post-training here."
