import time
import sys

lines = [
    "Loading 10%",
    "Loading 30%",
    "Loading 60%",
    "Loading 100%"
]

for i in range(len(lines)):
    sys.stdout.write("\r" + lines[i])
    sys.stdout.flush()
    time.sleep(1)

print()   # move to next line after loop