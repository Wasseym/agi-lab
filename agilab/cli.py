import typer
from agilab.train.sft import run as run_sft
from agilab.train.dpo import run as run_dpo
from agilab.train.prm import run as run_prm
from agilab.eval.harness import eval_main

app = typer.Typer(help="agilab — research ops CLI")

@app.command()
def sft(config: str = "configs/train/sft.yaml"):
    run_sft(config)

@app.command()
def dpo(config: str = "configs/train/dpo.yaml"):
    run_dpo(config)

@app.command()
def prm(config: str = "configs/train/prm.yaml"):
    run_prm(config)

@app.command()
def eval(config: str = "configs/eval/mmlu.yaml"):
    eval_main(config)

if __name__ == "__main__":
    app()
