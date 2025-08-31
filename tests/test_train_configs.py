def test_configs_exist():
    import os
    assert os.path.exists("configs/train/dpo.yaml")
    assert os.path.exists("configs/train/sft.yaml")
