filename = input("Enter the file name: ")
try:
    with open(filename, "r") as f:
        count = 0
        total = 0
        for line in f:
            if line.startswith("X-DSPAM-Confidence:"):
                count += 1
                confidence = float(line.split(":")[1])
                total += confidence
        if count > 0:
            print("Average spam confidence:", total / count)
except FileNotFoundError:
    print("File cannot be opened:", filename)