import os
for dirpath, dirnames, filenames in os.walk("."):
    print("Current Path:", dirpath)
    print("Directories:", dirnames)
    print("Files:", filenames)
