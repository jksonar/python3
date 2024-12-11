# Filtering with Absolute Paths

import glob

files = glob.glob("/home/user/*.txt")  # Match `.txt` files in a specific directory
print(files)
