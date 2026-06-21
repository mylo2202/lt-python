"""
Exercise 1: Write a simple program to simulate the operation of the grep
command on Unix. Ask the user to enter a regular expression and count the
number of lines that matched the regular expression.
"""

import re
from pathlib import Path


DATA_FILE = Path(__file__).resolve().parent / "mbox.txt"

regex = input("Enter a regular expression: ")
count = 0

try:
    with DATA_FILE.open("r", encoding="utf-8") as fhand:
        for line in fhand:
            if re.search(regex, line):
                count += 1
except FileNotFoundError:
    print("File cannot be opened:", DATA_FILE)
    exit()
except re.error:
    print("Invalid regular expression:", regex)
    exit()

print(f"mbox.txt had {count} lines that matched {regex}")
