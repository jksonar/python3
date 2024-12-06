# Get Modification Time
import os
import time

mod_time = os.path.getmtime('file.txt')
print("Last Modified Time:", time.ctime(mod_time))
