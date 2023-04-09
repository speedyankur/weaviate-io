# import subprocess
# import pytest
# from utils import *


# @pytest.fixture(scope="session")
# def setup_and_teardown(request):
#     # Code to run at startup
#     print("Spinning up Weaviate")
#     subprocess.run(["tests/start-weaviate.sh"])

#     def teardown():
#         # Code to run at exit
#         print("Shutting down Weaviate")
#         subprocess.run(["tests/stop-weaviate.sh"])

#     request.addfinalizer(teardown)


# script_paths = [
#     "./_includes/code/wcs.client.instantiation.mdx",
#     "./_includes/code/quickstart.autoschema.minimum.schema.mdx",
#     "./_includes/schema-delete-class.mdx",
#     "./_includes/code/quickstart.autoschema.connect.withkey.mdx",
#     "./_includes/code/quickstart.autoschema.import.mdx",
# ]

# @pytest.mark.parametrize("script_path", script_paths)
# def test_individual(script_path, setup_and_teardown):
#     parse_and_run(script_path)

# def test_sequential(setup_and_teardown):
#     for script in [
#         "./_includes/code/quickstart.autoschema.endtoend.mdx",
#         "./_includes/code/quickstart.autoschema.neartext.mdx",
#     ]:
#         parse_and_run(script)
