#Project: Number Guessing Game
#Step 1: Generate a random number
import random
number_to_guess = random.randint(1, 100)
#Step 2: Prompt the user for guesses
guess = int(input("Guess a number between 1 and 100: "))
number_of_attempts = 1
while guess != number_to_guess:
    if number_of_attempts >= 10:
        break
    if guess < number_to_guess:
        print("Too low! Try again.")
    else:
        print("Too high! Try again")
    number_of_attempts += 1
    guess = int(input("Guess a number between 1 and 100: "))
if number_of_attempts >= 10:
    print("Game over! Better luck next time!")
else:
    print("Congratulations! You've guessed the number in", number_of_attempts, "attempts.")
