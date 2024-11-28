import os
statvfs = os.statvfs("/")
total_space = statvfs.f_frsize * statvfs.f_blocks  # Total space
free_space = statvfs.f_frsize * statvfs.f_bfree  # Free space
used_space = total_space - free_space  # Used space

print(f"Total Space: {total_space // (1024**3)} GB")
print(f"Free Space: {free_space // (1024**3)} GB")
print(f"Used Space: {used_space // (1024**3)} GB")
