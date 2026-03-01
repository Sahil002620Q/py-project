import time
import winsound
import sys


for i in range(5,0,-1): 
    sys.stdout.write(f"\r 00:0{i}")
    sys.stdout.flush()
    time.sleep(1)
   

    
winsound.Beep(1000,500)
sys.stdout.write("\r  ")
sys.stdout.flush()
print("boom!")

#done