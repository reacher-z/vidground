#!/usr/bin/env python
"""CLI entry point: filter a JSONL dataset down to visually grounded examples."""

import argparse
import json
from pathlib import Path

from vidground.filter import Example, is_visually_grounded


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input",  type=Path, required=True, help="Input JSONL file.")
    parser.add_argument("--output", type=Path, required=True, help="Output JSONL file.")
    args = parser.parse_args()

    args.output.parent.mkdir(parents=True, exist_ok=True)
    kept = 0
    total = 0
    with args.input.open() as f_in, args.output.open("w") as f_out:
        for line in f_in:
            total += 1
            row = json.loads(line)
            ex = Example(
                id=row["id"],
                question=row["question"],
                options=row.get("options", []),
                answer=row["answer"],
            )
            if is_visually_grounded(ex):
                f_out.write(line)
                kept += 1

    print(f"kept {kept}/{total} ({kept / max(total, 1):.1%}) visually grounded examples")


if __name__ == "__main__":
    main()
