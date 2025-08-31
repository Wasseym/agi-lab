from transformers import AutoModelForCausalLM, AutoTokenizer

def load(base: str, load_4bit: bool = False):
    tok = AutoTokenizer.from_pretrained(base, use_fast=True)
    tok.pad_token = tok.eos_token
    model = AutoModelForCausalLM.from_pretrained(base)
    # TODO: wire 4-bit and FlashAttention if available
    return model, tok
