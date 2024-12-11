import glob
import os 

# a. Delete All .tmp Files
for file in glob.glob("*.tmp"):
    os.remove(file)


# b. Process Files in a Batch
for file in glob.glob("data/*.csv"):
    with open(file, "r") as f:
        content = f.read()
        print(f"Processing file: {file}")

# c. Combine glob with Regular Expressions
import re
files = glob.glob("data/*.txt")
filtered_files = [f for f in files if re.match(r".*2023.*", f)]  # Match files containing '2023'
print(filtered_files)
