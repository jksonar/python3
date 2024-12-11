# Recursive Search
# To search in subdirectories, use the ** pattern with recursive=True
import glob

files = glob.glob("**/*.py", recursive=True)  # Find all `.py` files in current and subdirectories
print(files)


#  Recursive Search Example
# To search for files in all subdirectories:

files = glob.glob("/home/user/**/*.log", recursive=True)  # Find all `.log` files
print(files)
