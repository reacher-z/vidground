# Data

This directory holds dataset preparation scripts and instructions.

## Layout
```
data/
├── raw/        # original downloaded datasets (gitignored)
└── filtered/   # VidGround-filtered subsets (gitignored)
```

## Supported datasets
TODO — list source datasets used in the paper (post-training corpora + eval benchmarks) with download links.

## Expected format
Each example should be a JSON line with at minimum:
```json
{
  "id": "...",
  "video": "path/to/video.mp4",
  "question": "...",
  "options": ["A", "B", "C", "D"],
  "answer": "B"
}
```

## Filtering
See [`../scripts/filter_visually_grounded.py`](../scripts/filter_visually_grounded.py).
