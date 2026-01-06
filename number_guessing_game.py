"""
Task 2: Number Guessing Game (Basic Version)

Description:
The program randomly generates a number between 1 and 100.
The user tries to guess the number within a limited number
of attempts. Feedback is provided for each guess.
"""

import random

# Generate a random number between 1 and 100
secret_number = random.randint(1, 100)

# Maximum number of attempts
max_attempts = 5
attempts = 0

print("Welcome to the Number Guessing Game!")
print("I have selected a number between 1 and 100.")
print(f"You have {max_attempts} attempts to guess it.\n")

# Loop until attempts are over
while attempts < max_attempts:
    try:
        guess = int(input("Enter your guess: "))
        attempts += 1

        if guess < secret_number:
            print("Too low! Try Again.\n")
        elif guess > secret_number:
            print("Too high! Try Again.\n")
        else:
            print(f"Congratulations! You guessed the number in {attempts} attempts.")
            break

    except ValueError:
        print("Please enter a valid integer.\n")

# If user fails to guess within attempts
if attempts == max_attempts and guess != secret_number:
    print(f"Game Over! The correct number was {secret_number}.")
