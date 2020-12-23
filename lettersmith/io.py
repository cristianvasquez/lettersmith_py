"""
File utilities
"""
from pathlib import Path


def write_file_deep(pathlike, content, mode="w"):
    """Write a file to filepath, creating directories if necessary"""
    file_path = Path(pathlike)
    file_path.parent.mkdir(exist_ok=True, parents=True)
    with open(file_path, mode) as f:
        f.write(content)
