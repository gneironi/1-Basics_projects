#The number guessing game is a popular game among programmers. 
#In the number guessing game, the program selects a random number between two numbers, 
#and the user guesses the correct number.


#TODO: select a random number between 1 and 10.

import random

n = random.randrange(1,10)
guess = int(input("Enter a number: "))
while n!= guess:
    if guess < n:
        print("This number is too low")
        guess = int(input("Try again: "))
    elif guess > n:
        print("This number is too high")
        guess = int(input("Try again: "))
    else:
        break
print("You guesses it right!!, Congrats!")

#tools used:
#import libreries, loops, conditionals, print, input, change value type int()
