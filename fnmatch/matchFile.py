import fnmatch
import os

for file in os.listdir('.'):
    if fnmatch.fnmatch(file, '*.py'):
        print(f"Python script: {file}")
