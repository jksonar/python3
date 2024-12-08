import shutil

shutil.copy("source.txt", "destination.txt")

# Copy File with Metadata using copy2 

shutil.copy2("source.txt", "destination.txt")


# Copy a Directory

shutil.copytree("source_directory", "destination_directory")
