import fnmatch
import os

files = ['report1.txt', 'data.csv', 'summary.log', 'backup.tar.gz']

# Match all .txt files
txt_files = fnmatch.filter(files, '*.txt')
print(txt_files)  # ['report1.txt']
