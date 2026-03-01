import time
import random
import sys
x = ['rock','paper','scissor']
p1 = random.choice(x)
p2 = random.choice(x)
  
u1 = input('enter user 1 : \n')
u2 = input('enter user 2 : \n')



for i in range(10):
       dot = "."*(i%4)
       sys.stdout.write("\rrolling"+dot+" ")
       sys.stdout.flush()
       time.sleep(0.5)

       sys.stdout.write("\r")
       sys.stdout.flush()

print(u1,' got ',p1)
time.sleep(0.5)
print(u2,' got ',p2)

if p1 == 'rock' and p2 == 'scissor':
    print(u1,' wins ')
    time.sleep(0.5)
    print(u2,' looses ')
elif p1 == 'scissor' and p2 == 'paper':
        print(u1,' wins ')
        time.sleep(0.5)
        print(u2,' looses ')
elif p1 == 'paper' and p2 == 'rock':
        print(u1,' wins ')
        time.sleep(0.5)
        print(u2,' looses ')
elif p1 == p2:
        print('it is a tie') # write it's rather than it is
else:
        print(u2,' wins ')
        time.sleep(0.5)
        print(u1,' looses ')
# else:
#     print('Wasted')