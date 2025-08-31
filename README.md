# agi-lab — private research monorepo

A pragmatic research monorepo to iterate on **reasoning**, **data quality**, **efficient training**,
**agents/tool-use**, and **interpretability** with modest compute.

## Quickstart
```bash
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install --upgrade pip
pip install -e .
# (Optional) Install CUDA-specific Torch build per your GPU.
# pip install --index-url https://download.pytorch.org/whl/cu124 torch torchvision torchaudio

make dpo     # sanity stub run
make eval    # eval stub
```

## Layout
See inline directories and `configs/` for Hydra-based runs. Stubs compile on CPU.
