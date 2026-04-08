# VidGround

> **Watch Before You Answer: Learning from Visually Grounded Post-Training**

[![arXiv](https://img.shields.io/badge/arXiv-2604.05117-b31b1b.svg)](https://arxiv.org/abs/2604.05117)
[![HF Paper](https://img.shields.io/badge/%F0%9F%A4%97-Paper-yellow)](https://huggingface.co/papers/2604.05117)
[![Project Page](https://img.shields.io/badge/Project-Page-blue)](http://vidground.etuagi.com)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

## TL;DR
Many "video" benchmarks and post-training datasets can be solved **without watching the video**. We show that **40–60%** of questions in commonly used long-video benchmarks are answerable from text alone, and that the same bias pervades widely used post-training datasets. Filtering down to *visually grounded* questions only — what we call **VidGround** — improves RL post-training by up to **+6.2 points** while using only **69.1%** of the original data.

## Key findings
- 📉 **40–60%** of questions in popular long-video benchmarks are answerable from text alone.
- 🧹 Filtering for visually grounded questions yields a smaller (**69.1%** of original) but cleaner training set.
- 🚀 Combined with vanilla RL post-training, VidGround improves accuracy by up to **+6.2 points**.
- 🏆 Simple data curation **beats** several more sophisticated post-training techniques.

## Repository structure
```
vidground/
├── README.md
├── LICENSE
├── pyproject.toml
├── citation.bib
├── data/                          # dataset preparation instructions
│   └── README.md
├── eval/                          # evaluation protocol notes
│   └── README.md
├── scripts/
│   ├── filter_visually_grounded.py
│   └── run_rl_posttrain.sh
└── src/vidground/
    ├── __init__.py
    ├── filter.py                  # text-only-solvability filtering
    └── eval.py                    # eval helpers
```

## Installation
```bash
git clone https://github.com/TODO/vidground.git
cd vidground
pip install -e .
```

## Quick start

### 1. Prepare data
See [`data/README.md`](data/README.md) for dataset download and formatting instructions.

### 2. Filter for visually grounded questions
```bash
python scripts/filter_visually_grounded.py \
    --input  data/raw/your_dataset.jsonl \
    --output data/filtered/your_dataset.vidground.jsonl
```

### 3. RL post-training
```bash
bash scripts/run_rl_posttrain.sh
```

### 4. Evaluation
See [`eval/README.md`](eval/README.md).

## Results
<!-- TODO: drop in headline numbers from the paper -->
| Model | Data | VideoMME | LongVideoBench | Notes |
|-------|------|---------:|---------------:|-------|
| Baseline (full data) | 100% | — | — | TODO |
| **+ VidGround filter** | 69.1% | **+6.2** | TODO | TODO |

## Citation
If you find this work useful, please cite:
```bibtex
@article{zhang2025vidground,
  title   = {Watch Before You Answer: Learning from Visually Grounded Post-Training},
  author  = {Zhang, Yuxuan and Hwang, EunJeong and Zhang, Huaisong and Du, Penghui
             and Jia, Yiming and Jiang, Dongfu and He, Xuan and Zhang, Shenhui
             and Nie, Ping and West, Peter and Allen, Kelsey R.},
  journal = {arXiv preprint arXiv:2604.05117},
  year    = {2026}
}
```

## Acknowledgements
We thank our collaborators at UBC, Vector Institute, Etude AI, Kuaishou (Kolors Team), University of Toronto, University of Waterloo, and UIUC.

## License
Released under the [MIT License](LICENSE).
