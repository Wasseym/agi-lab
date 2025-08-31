def test_eval_stub():
    from agilab.eval.harness import eval_main
    assert callable(eval_main)
