import os

output = os.popen("ls -l").read()
print("Command Output:")
print(output)
