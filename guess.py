low = 1 
high = 100

while low <= high:
    guess = (low + high) // 2
    print("guess a number ")

    print('if number is greater enter g, if smaller then s, if same the y')
    print('is it',guess)
    you = input('what is  it ')

    if you == 'c':
        print(' AI guessed it it is ',guess)
        break 

    elif you == 'g':
        high = guess - 1 

    elif you == 's':
        low = guess + 1

    else:
        print("you'r number is ",guess)
    