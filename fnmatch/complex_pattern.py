# Complex Patterns (Wildcard and Brackets)
import fnmatch

files = ['report1.doc', 'report2.doc', 'summary.pdf', 'data.csv']

# Match report followed by any number
matches = fnmatch.filter(files, 'report[0-9].doc')
print(matches)  # ['report1.doc', 'report2.doc']
