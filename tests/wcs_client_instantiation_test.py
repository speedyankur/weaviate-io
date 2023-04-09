import utils


def test(anon_empty_weaviate):
    test_namespace = utils.run_script("_includes/code/wcs.client.instantiation.py")
    assert "classes" in test_namespace["schema"].keys()
