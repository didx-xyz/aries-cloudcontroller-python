import re
import sys


def clean_file(file_path):
    """This method cleans up decorators in api modules that have unnecessary validate_call decorators"""
    modified_lines = []

    with open(file_path, "r") as file:
        lines = file.readlines()

    i = 0
    while i < len(lines):
        if (
            lines[i].strip() == "@validate_call"
            and i + 1 < len(lines)
            and re.search(
                r"async def .*(?:_without_preload_content|_with_http_info)\(",
                lines[i + 1],
            )
        ):
            pass  # skip validate_call line because next line matches
        else:
            modified_lines.append(lines[i])
        i += 1

    with open(file_path, "w") as file:
        file.writelines(modified_lines)


if __name__ == "__main__":
    # Expecting the first argument to be the file path
    if len(sys.argv) > 1:
        clean_file(sys.argv[1])
    else:
        print("Usage: python clean_decorators.py <path_to_file>")
