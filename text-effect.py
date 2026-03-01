import time 
info = ["do you want to proceed :",
        "yup"]

for line in info:
    for ch in line:
        print(ch,end="",flush=True)
        time.sleep(0.1)
    print()