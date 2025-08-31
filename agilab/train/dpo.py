from dataclasses import dataclass
import json, yaml
from transformers import AutoModelForCausalLM, AutoTokenizer
from trl import DPOTrainer

def _load_prefs(path):
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            j = json.loads(line)
            yield {"prompt": j["prompt"], "chosen": j["chosen"], "rejected": j["rejected"]}

def run(cfg_path: str):
    cfg = yaml.safe_load(open(cfg_path))
    mcfg, tcfg, dcfg = cfg["model"], cfg["train"], cfg["data"]

    tok = AutoTokenizer.from_pretrained(mcfg["base"], use_fast=True)
    tok.pad_token = tok.eos_token
    model = AutoModelForCausalLM.from_pretrained(mcfg["base"])

    train_ds = list(_load_prefs(dcfg["pref_dataset"]))

    trainer = DPOTrainer(
        model=model,
        args=dict(
            output_dir=tcfg["output_dir"],
            per_device_train_batch_size=tcfg["per_device_batch_size"],
            gradient_accumulation_steps=tcfg["grad_accum_steps"],
            num_train_epochs=tcfg["epochs"],
            learning_rate=tcfg["lr"],
            warmup_ratio=tcfg["warmup_ratio"],
            bf16=tcfg["bf16"],
            logging_steps=tcfg["logging_steps"],
            save_steps=tcfg["save_steps"],
        ),
        train_dataset=train_ds,
        tokenizer=tok,
        beta=0.1,
    )
    print("[agilab] DPO training stub starting.")
    try:
        trainer.train()
    except Exception as e:
        print("[agilab] DPO stub ended (setup required).", e)
