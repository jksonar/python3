import os

file_path = "example.txt"
if os.name == "nt":  # Windows
    os.startfile(file_path)
elif os.name == "posix":  # macOS/Linux
    os.system(f"xdg-open {file_path}")

if os.name == "nt":
    print("Operating System: Windows")
elif os.name == "posix":
    print("Operating System: macOS/Linux")
