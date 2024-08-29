import re
import sys


def clean_file(file_path):
    """This method cleans up API modules by removing specific methods and their decorators"""
    modified_lines = []
    ignore_block = False

    with open(file_path, "r") as file:
        lines = file.readlines()

    i = 0
    while i < len(lines):
        if lines[i].strip() == "@validate_call":  # find decorator
            if i + 1 < len(lines) and re.search(
                r"async def .*(?:_without_preload_content|_with_http_info)\(",
                lines[i + 1],  # See if next line is unwanted method
            ):
                ignore_block = True
            else:
                ignore_block = False  # If not unwanted method, then include this block

        if (
            lines[i].strip().startswith("def ")
            or lines[i].strip().startswith("async def ")
            and not re.search(
                r"async def .*(?:_without_preload_content|_with_http_info)\(", lines[i]
            )
        ):
            ignore_block = False

        if not ignore_block:
            modified_lines.append(lines[i])

        i += 1

    with open(file_path, "w") as file:
        file.writelines(modified_lines)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        clean_file(sys.argv[1])
    else:
        print("Usage: python clean_file.py <path_to_file>")
