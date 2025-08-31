import yaml
from transformers import AutoModelForCausalLM, AutoTokenizer
from trl import SFTTrainer
from agilab.train.data_pipeline import load_sft_pairs

def run(cfg_path: str):
    cfg = yaml.safe_load(open(cfg_path))
    mcfg, tcfg, dcfg = cfg["model"], cfg["train"], cfg["data"]

    pairs = load_sft_pairs(dcfg["sft_dataset"])
    texts = [f"### Instruction\n{inp}\n### Response\n{out}" for inp, out in pairs]

    tok = AutoTokenizer.from_pretrained(mcfg["base"], use_fast=True)
    tok.pad_token = tok.eos_token
    model = AutoModelForCausalLM.from_pretrained(mcfg["base"])

    trainer = SFTTrainer(model=model, train_dataset=texts, tokenizer=tok)
    print("[agilab] SFT stub starting.")
    try:
        trainer.train()
    except Exception as e:
        print("[agilab] SFT stub ended (setup required).", e)
