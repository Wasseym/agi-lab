def test_import():
    import agilab.data_tools.dedup as d
    assert hasattr(d, "simhash")
