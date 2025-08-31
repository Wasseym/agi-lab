# Thin wrapper stub — wire into EleutherAI LM Eval Harness for real runs.
import yaml
def eval_main(cfg_path: str):
    cfg = yaml.safe_load(open(cfg_path))
    print(f"[agilab] Eval stub for task={cfg.get('task')} shots={cfg.get('shots')}")
