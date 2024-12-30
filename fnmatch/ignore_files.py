# Ignore Specific Files
import fnmatch

files = ['important.txt', 'temp.log', 'data.bak']

for file in files:
    if not fnmatch.fnmatch(file, '*.bak'):
        print(f"Processing: {file}")
