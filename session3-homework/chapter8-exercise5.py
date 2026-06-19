"""
Exercise 5: Write a program to read through the mail box data and
when you find line that starts with “From”, you will split the line into
words using the split function. We are interested in who sent the
message, which is the second word on the From line.
You will parse the From line and print out the second word for each
From line, then you will also count the number of From (not From:)
lines and print out a count at the end.
"""

fname = input("Enter a file name: ")
try:
    with open(fname, "r") as f:
        count = 0
        for line in f:
            if line.startswith("From "):
                count += 1
                email = line.split()[1]
                print(email)
        print("There were", count, "lines in the file with From as the first word")
except FileNotFoundError:
    print("File cannot be opened:", fname)