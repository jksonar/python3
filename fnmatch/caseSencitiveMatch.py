# Case-Insensitive Matching
import fnmatch

files = ['README.TXT', 'notes.md', 'script.PY', 'log.txt']

# Match .txt files (case insensitive)
matches = [f for f in files if fnmatch.fnmatchcase(f, '*.txt')]
print(matches)  # ['log.txt']

# fnmatch.fnmatchcase performs case-sensitive matching, unlike fnmatch.fnmatch which is case-insensitive on Windows.