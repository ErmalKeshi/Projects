# Guessing game

import random       # Importing random Library

true_nr = random.randint(1, 100)    # Generating a list with a random number.
guess_nr = 1       # Specifying nr of guest we want to type.( The lower the better.)
while True:        # Creating a while loop.
    guess = int(input(f"Guess : {guess_nr} "))  # Making sure that the value typed is an integer.
    guess_nr += 1

    if guess == true_nr:      # Specifying our conditions.
        print(f"Winner in {guess_nr} guesses.")     # If guess is right declare the winner and how many attempts.
        break
    elif guess > true_nr:
        print("The guess is lower!")
    else:
        print("The guess higher!")
    # Best of luck :) !!