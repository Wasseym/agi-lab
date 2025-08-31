def test_react():
    from agilab.agents.react import run
    out = run("hello")
    assert "react" in out
