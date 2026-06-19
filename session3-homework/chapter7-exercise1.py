"""
Exercise 1: Write a program to read through a file and print the contents
of the file (line by line) all in upper case.
"""

filename = input("Enter a file name: ")
try:
    with open(filename, "r") as f:
        print(f.read().upper())
except FileNotFoundError:
    print("File cannot be opened:", filename)
