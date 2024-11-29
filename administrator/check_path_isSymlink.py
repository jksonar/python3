import os

path = "example_symlink"
if os.path.islink(path):
    print("It's a symbolic link.")
else:
    print("It's not a symbolic link.")
