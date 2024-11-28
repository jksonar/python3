import os

dir_fd = os.open(".", os.O_RDONLY)
files = os.listdir(dir_fd)
os.close(dir_fd)
print("Files:", files)
