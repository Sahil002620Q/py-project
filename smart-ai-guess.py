low = 1
high = 100
print("Think of a number between 1 and 100.")

while True:
    guess = (low + high) // 2
    print("Is your number:", guess)
    
    feedback = input("Enter 'h' if too high, 'l' if too low, 'c' if correct: ")
    
    if feedback == 'c':
        print("Yay! AI guessed your number!")
        break
    elif feedback == 'h':
        high = guess - 1
    elif feedback == 'l':
        low = guess + 1
    else:
        print("Invalid input")