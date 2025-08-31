# Process Reward Model training stub
import yaml
from transformers import AutoModelForSequenceClassification, AutoTokenizer, TrainingArguments, Trainer
from datasets import Dataset

def run(cfg_path: str):
    # Use a tiny synthetic dataset for the stub; replace with real steps dataset.
    texts = [
        "Step: let x=2; compute x+x -> 4. Label=good",
        "Step: hallucinate a number without reasoning. Label=bad",
    ]
    labels = [1, 0]
    ds = Dataset.from_dict({"text": texts, "label": labels})

    base = "distilbert-base-uncased"
    tok = AutoTokenizer.from_pretrained(base)
    def tok_fn(ex): return tok(ex["text"], truncation=True, max_length=256)
    ds_tok = ds.map(tok_fn, batched=True)
    model = AutoModelForSequenceClassification.from_pretrained(base, num_labels=2)

    args = TrainingArguments(
        output_dir="runs/prm_stub",
        per_device_train_batch_size=2,
        num_train_epochs=1,
        learning_rate=1e-5,
        logging_steps=5,
    )
    print("[agilab] PRM training stub starting.")
    Trainer(model, args, train_dataset=ds_tok).train()
