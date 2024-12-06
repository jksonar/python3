# Walk Through a Directory
import os

for root, dirs, files in os.walk('.'):
    print("Root:", root)
    print("Directories:", dirs)
    print("Files:", files)
