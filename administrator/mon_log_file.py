# Monitor Logs (Tail a File)
import time

def tail_log(file_path):
    with open(file_path, "r") as f:
        f.seek(0, 2)  # Move to the end of the file
        while True:
            line = f.readline()
            if line:
                print(line.strip())
            time.sleep(1)

tail_log("/var/log/syslog")
