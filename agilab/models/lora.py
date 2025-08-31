# Placeholder hooks to apply LoRA via PEFT
from peft import LoraConfig, get_peft_model

def apply_lora(model, r=16, alpha=32, dropout=0.05):
    cfg = LoraConfig(r=r, lora_alpha=alpha, lora_dropout=dropout, target_modules=["q_proj","v_proj"])
    return get_peft_model(model, cfg)
