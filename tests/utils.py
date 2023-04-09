import os
import re
from pathlib import Path


def preprocess_codeblock(raw_codeblock: str) -> str:
    """
    Replaces placeholder text such as the URL and API keys with testable equivalents.

    Args:
        raw_codeblock (str): The raw code block from the markdown file.

    Returns:
        str: The preprocessed code block with placeholders replaced.
    """
    # Replace URL
    proc_codeblock = raw_codeblock
    for rep_tuple in [
        [
            "http://localhost:8080",
            "http://localhost:8099",
        ],  # Specify different port to usual to avoid confusion
        ["https://some-endpoint.weaviate.network", "http://localhost:8099"],
    ]:
        proc_codeblock = proc_codeblock.replace(*rep_tuple)

    # Replace OpenAI key
    pattern = r'"X-OpenAI-Api-Key": "(.+?)"'
    my_api_key = os.environ["OPENAI_API_KEY"]
    proc_codeblock = re.sub(
        pattern, f'"X-OpenAI-Api-Key": "{my_api_key}"', proc_codeblock
    )
    return proc_codeblock


def extract_code_blocks(file_path: Path, regex_pattern: re.Pattern) -> list:
    """
    Extracts Code blocks from a markdown file.

    Args:
        file_path (Path): The path to the markdown file.

    Returns:
        list: A list containing extracted code blocks.
    """

    with file_path.open() as file:
        content = file.read()
        code_blocks = regex_pattern.findall(content)

        extracted_blocks = []

        for block in code_blocks:
            extracted_blocks.append(block.strip())

        return extracted_blocks


def extract_language_code_blocks(file_path: Path, lang_code: str = "python") -> list:
    code_block_regex = re.compile(
        rf"```{lang_code}\n(.*?)\n```", re.DOTALL | re.MULTILINE
    )

    return extract_code_blocks(file_path, code_block_regex)


def extract_test_code_blocks(file_path: Path) -> list:
    """
    Extracts Python code blocks and associated HTML comments from a markdown file.

    Args:
        file_path (Path): The path to the markdown file.

    Returns:
        list: A list of dictionaries containing extracted code blocks and associated comments.
    """
    code_block_regex = re.compile(
        r"<!--\s*(.+?)\s*-->\n?```python\n(.*?)\n```\n?<!--\s*(.+?)\s*-->",
        re.DOTALL | re.MULTILINE,
    )

    code_blocks = extract_code_blocks(file_path, code_block_regex)

    extracted_blocks = list()
    for code_block in code_blocks:
        extracted_blocks.append(
            {
                "preparation": preprocess_codeblock(code_block[0].strip()),
                "code": preprocess_codeblock(code_block[1]),
                "test_assertion": code_block[2].strip(),
            }
        )
    return extracted_blocks


# def extract_test_code_blocks(file_path: Path) -> dict:
#     """
#     Extracts Python code blocks and associated HTML comments from a markdown file.

#     Args:
#         file_path (Path): The path to the markdown file.

#     Returns:
#         dict: A dictionary containing extracted code blocks and associated comments.
#     """
#     code_block_regex = re.compile(r'<!--\s*(.+?)\s*-->\n?```python\n(.*?)\n```\n?<!--\s*(.+?)\s*-->', re.DOTALL | re.MULTILINE)

#     with file_path.open() as file:
#         content = file.read()
#         code_blocks = code_block_regex.findall(content)

#         extracted_blocks = []

#         for block in code_blocks:
#             extracted_blocks.append({
#                 "preparation": preprocess_codeblock(block[0].strip()),
#                 "code": preprocess_codeblock(block[1]),
#                 "test_assertion": block[2].strip(),
#             })

#         return extracted_blocks


def process_markdown_files(dir_path: str) -> list:
    """
    Processes all markdown files in the specified directory, extracting code blocks and associated comments.

    Args:
        dir_path (str): The path to the directory containing markdown files.

    Returns:
        list: A list of dictionaries containing extracted code blocks and associated comments.
    """
    all_blocks = []

    for file_path in Path(dir_path).rglob("*.md"):
        all_blocks.extend(extract_test_code_blocks(file_path))

    return all_blocks


def parse_and_run(script_path: str) -> None:
    """
    Parses the specified markdown file, extracts the code blocks, and runs the code with associated tests.

    Args:
        script_path (str): The path to the markdown file.
    """
    print(f"Testing {script_path}")
    startpath = Path(script_path)
    codeblocks = extract_test_code_blocks(startpath)
    codeblocks

    for codeblock in codeblocks:
        print(f"Found a code block {len(script_path)} lines long...")
        exec(codeblock["preparation"])
        print(f"Running code...")
        exec(codeblock["code"])
        print(f"Testing: \n==========\n{codeblock['test_assertion']}\n==========\n")
        exec(codeblock["test_assertion"])


def run_script(script_path):
    with open(script_path, "r") as f:
        script_txt = f.read()
    proc_script = preprocess_codeblock(script_txt)

    namespace = {}
    exec(proc_script, namespace)
    return namespace
