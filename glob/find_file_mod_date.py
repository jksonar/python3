
import glob
import os

# Find Files by Modification Date
# To sort or filter by modification date:

files = glob.glob("*.txt")
sorted_files = sorted(files, key=os.path.getmtime)  # Sort by modification time
print(sorted_files)
