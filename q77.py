#number guessing game
import random

def play_game():
    target_number = random.randint(1, 100)
    attempts = 0

    while True:
        guess = int(input("Guess a number between 1 and 100: "))
        attempts += 1

        if guess == target_number:
            print("Congratulations! You guessed the correct number.")
            print("Attempts:", attempts)
            break
        elif guess < target_number:
            print("Too low! Try again.")
        else:
            print("Too high! Try again.")

print("Number Guessing Game")
play_game()
