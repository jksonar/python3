import glob

# a. Match Any Character (*)

files = glob.glob("*.txt")  # Matches any file ending with `.txt`
print(files)

# b. Match a Single Character (?)

files = glob.glob("file?.py")  # Matches `file1.py`, `file2.py`, etc., but not `file10.py`
print(files)

# c. Match a Set of Characters ([])

files = glob.glob("data/file[1-3].csv")  # Matches `file1.csv`, `file2.csv`, `file3.csv`
print(files)
