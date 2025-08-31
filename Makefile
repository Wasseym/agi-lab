.PHONY: setup fmt lint test sft dpo prm moe eval dedup contam

setup:
	bash scripts/bootstrap.sh

fmt:
	ruff check --fix . && black .

lint:
	ruff check .

test:
	pytest -q || true

sft:
	agilab sft --config configs/train/sft.yaml || true

dpo:
	agilab dpo --config configs/train/dpo.yaml || true

prm:
	agilab prm --config configs/train/prm.yaml || true

moe:
	python agilab/models/moe.py || true

eval:
	agilab eval --config configs/eval/mmlu.yaml || true

dedup:
	python agilab/data_tools/dedup.py || true

contam:
	python agilab/data_tools/contam.py || true
