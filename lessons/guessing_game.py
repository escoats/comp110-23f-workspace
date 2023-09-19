'''program that loops until correct number is guessed'''
# 9.19.2023 in-class practice
# guessing game

from random import randint

secret: int = randint(1, 10)
guess: int = int(input("Guess a number between 1 and 10: "))
num_tries: int = 0
max_tries: int = 3

while (guess != secret) and (num_tries <= max_tries - 1):
    print("Wrong!")
    # If guess is out of bounds, let them know
    if guess < 1 or guess > 10:
        print("That's not between 1 and 10!")
    # If guess is too low, tell them
    if guess < secret:
        print("Too low!")
    # If guess is too high, tell them
    else: 
        print("Too high!")
    guess = int(input("Guess again: "))
    num_tries += 1

if guess == secret:
    print("You guessed correctly!")
else: 
    print("You lose :(")
