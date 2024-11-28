import os
import shutil

# if directory is empty then only we can remove directory
os.rmdir("new_folder")
print("Directory removed.")

# If Directory is not empty then use shutil module
shutil.rmtree("new_folder")
print("Directory removed.")
