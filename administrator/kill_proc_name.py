import os

def kill_process(name):
    os.system(f"pkill -f {name}")
    print(f"Processes matching '{name}' terminated.")

kill_process("python")
