import psutil

# Get Virtual Memory Info
memory_info = psutil.virtual_memory()
print(f"Total Memory: {memory_info.total // (1024 ** 2)} MB")
print(f"Used Memory: {memory_info.used // (1024 ** 2)} MB")
print(f"Available Memory: {memory_info.available // (1024 ** 2)} MB")

# Get Swap Memory Info
swap_info = psutil.swap_memory()
print(f"Total Swap: {swap_info.total // (1024 ** 2)} MB")
print(f"Used Swap: {swap_info.used // (1024 ** 2)} MB")
