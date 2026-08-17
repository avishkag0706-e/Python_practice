'''DAY 3'''

# The computer chooses a random number between 1 and 100.
# The user keeps guessing until they get it right.
# limit only 5 attempts

import random

# Computer chooses a random number
num = random.randint(1,100)
print(num)
print("GUESS THE NUMBER GAME")
print("I have guess the number between 1 to 100")
print("You got 5 attempt to trybest of luck\n")
attempt = 0
while True:
    guess = int(input("Guess YOUR number:"))
    attempt +=1
    
    if guess<num:
        print(attempt,"attempt:too low! Try again!!\n")
        
    elif guess>num:
        print(attempt,"attempt:Too high! Try again\n")
        
    else:
        print("You won!! in ",attempt,"attempts")
        break
    if attempt ==5:
        print("you are out of limit")
        break
    