from pathlib import Path
import json

def read_jsonl(path):
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            yield json.loads(line)

def ensure_dir(p):
    Path(p).mkdir(parents=True, exist_ok=True)
