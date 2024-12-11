# Using glob.iglob
# The iglob function works like glob but returns an iterator instead of a list. It is more memory-efficient for large results.

import glob
    
for file in glob.iglob("*.txt"):
    print(file)
