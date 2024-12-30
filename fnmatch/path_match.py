# Full Path Matching
import fnmatch

paths = ['/home/user/report1.txt', '/var/log/syslog', '/home/user/data.csv']

matches = [p for p in paths if fnmatch.fnmatch(p, '/home/user/*.txt')]
print(matches)  # ['/home/user/report1.txt']
