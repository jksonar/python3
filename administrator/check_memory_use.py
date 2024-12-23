import psutil

def memory_usage():
    memory = psutil.virtual_memory()
    print(f"Total: {memory.total // (1024**3)} GB")
    print(f"Available: {memory.available // (1024**3)} GB")
    print(f"Used: {memory.used // (1024**3)} GB")
    print(f"Usage: {memory.percent}%")

memory_usage()
