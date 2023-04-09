import utils


def test_tutorial_scripts(anon_empty_weaviate):
    # ===== INIT TEST ENV =====
    proc_script = utils.parse_and_prep_script(
        "_includes/code/quickstart.schema.create.mdx"
    )
    test_namespace = {}

    # ===== PRE-TEST SCRIPT =====
    # e.g. import weaviate
    # ===== RUN SCRIPT =====
    exec(proc_script, globals(), test_namespace)
    # ===== RUN TEST =====
    schema = test_namespace["schema"]
    class_names = [c["class"] for c in schema["classes"]]
    assert "Question" in class_names
    for c in schema["classes"]:
        if c["class"] == "Question":
            break
    for pname in ["question", "answer", "category"]:
        assert pname in [prop["name"] for prop in c["properties"]]

    # ===== INIT TEST ENV =====
    proc_script = utils.parse_and_prep_script(
        "_includes/code/quickstart.import.questions.mdx"
    )

    # ===== RUN SCRIPT =====
    exec(proc_script, globals(), test_namespace)

    # ===== RUN TEST =====
    client = test_namespace["client"]
    assert (
        client.query.aggregate("Question")
        .with_meta_count()
        .do()["data"]["Aggregate"]["Question"][0]["meta"]["count"]
        == 10
    )

    # ===== INIT TEST ENV =====
    proc_script = utils.parse_and_prep_script(
        "_includes/code/quickstart.import.get.mdx"
    )

    # ===== RUN SCRIPT =====
    exec(proc_script, globals(), test_namespace)

    # ===== RUN TEST =====
    some_objects = test_namespace["some_objects"]
    assert len(some_objects["objects"]) == 10
    assert some_objects["objects"][0]["class"] == "Question"

    # ===== INIT TEST ENV =====
    proc_script = utils.parse_and_prep_script(
        "_includes/code/quickstart.query.neartext.additional.mdx"
    )

    # ===== RUN SCRIPT =====
    exec(proc_script, globals(), test_namespace)

    # ===== RUN TEST =====
    results = test_namespace["results"]
    assert len(results["data"]["Get"]["Question"]) == 2
    assert results["data"]["Get"]["Question"][0]["answer"] == "DNA"
    assert results["data"]["Get"]["Question"][1]["answer"] == "species"
    assert "certainty" in results["data"]["Get"]["Question"][0]["_additional"]

    # ===== INIT TEST ENV =====
    proc_script = utils.parse_and_prep_script(
        "_includes/code/quickstart.query.where.1.mdx"
    )

    # ===== RUN SCRIPT =====
    exec(proc_script, globals(), test_namespace)

    # ===== RUN TEST =====
    results = test_namespace["results"]
    assert len(results["data"]["Get"]["Question"]) == 4

    # ===== INIT TEST ENV =====
    proc_script = utils.parse_and_prep_script(
        "_includes/code/quickstart.query.where.2.mdx"
    )

    # ===== RUN SCRIPT =====
    exec(proc_script, globals(), test_namespace)

    # ===== RUN TEST =====
    results = test_namespace["results"]
    assert len(results["data"]["Get"]["Question"]) == 2
    assert results["data"]["Get"]["Question"][0]["answer"] == "the nose or snout"
    assert results["data"]["Get"]["Question"][-1]["answer"] == "Elephant"

    # ===== INIT TEST ENV =====
    proc_script = utils.parse_and_prep_script(
        "_includes/code/quickstart.query.aggregate.1.mdx"
    )

    # ===== RUN SCRIPT =====
    exec(proc_script, globals(), test_namespace)

    # ===== RUN TEST =====
    results = test_namespace["results"]
    assert results["data"]["Aggregate"]["Question"][0]["meta"]["count"] == 10

    # ===== INIT TEST ENV =====
    proc_script = utils.parse_and_prep_script(
        "_includes/code/quickstart.query.aggregate.2.mdx"
    )

    # ===== RUN SCRIPT =====
    exec(proc_script, globals(), test_namespace)

    # ===== RUN TEST =====
    results = test_namespace["results"]
    assert results["data"]["Aggregate"]["Question"][0]["meta"]["count"] == 4
