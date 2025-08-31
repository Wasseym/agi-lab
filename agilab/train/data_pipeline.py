from agilab.utils.io import read_jsonl

def load_sft_pairs(path):
    return [(j["input"], j["output"]) for j in read_jsonl(path)]
