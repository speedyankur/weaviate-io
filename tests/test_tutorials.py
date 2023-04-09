import os
import utils


def test_template(anon_empty_weaviate):
    # ===== INIT TEST ENV =====
    proc_script = utils.parse_and_prep_script(
        "path/to/script"
    )
    test_namespace = {}

    # ===== PRE-TEST SCRIPT =====
    # e.g. import weaviate
    # ===== RUN SCRIPT =====
    # exec(proc_script, globals(), test_namespace)
    # ===== RUN TEST =====
    # assert ...