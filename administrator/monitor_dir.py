import os
import time

watched_dir = "."
print("Monitoring directory:", watched_dir)
before = set(os.listdir(watched_dir))

while True:
    time.sleep(2)
    after = set(os.listdir(watched_dir))
    added = after - before
    removed = before - after
    if added:
        print("Added:", added)
    if removed:
        print("Removed:", removed)
    before = after
