"""
Exercise 2: Look for lines of the form "New Revision: 39772".
Extract the number using a regular expression and findall(), then print
the average as an integer.
"""

import re
from pathlib import Path


DATA_DIR = Path(__file__).resolve().parents[1] / "session3-homework"


def resolve_filename(filename):
    path = Path(filename)
    if path.exists():
        return path

    data_path = DATA_DIR / filename
    if data_path.exists():
        return data_path

    return path


filename = input("Enter file:")
path = resolve_filename(filename)
revision_numbers = []

try:
    with path.open("r", encoding="utf-8") as fhand:
        for line in fhand:
            matches = re.findall(r"^New Revision: ([0-9]+)", line)
            for match in matches:
                revision_numbers.append(int(match))
except FileNotFoundError:
    print("File cannot be opened:", filename)
    exit()

if len(revision_numbers) == 0:
    print("No revision numbers found.")
else:
    average = sum(revision_numbers) / len(revision_numbers)
    print(int(average))
