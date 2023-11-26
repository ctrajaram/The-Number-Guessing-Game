"""
Python Development Techdegree
Project 1 - The Number Guessing Game
--------------------------------
"""

# Import the random module.

# Create the start_game function.
# Write your code inside this function.

#   When the program starts, we want to:
#   ------------------------------------
#   1. Display an intro/welcome message to the player.
#   2. Store a random number as the answer/solution.
#   3. Continuously prompt the player for a guess.
#     a. If the guess is greater than the solution, display to the player "It's lower".
#     b. If the guess is less than the solution, display to the player "It's higher".

#   4. Once the guess is correct, stop looping, inform the user they "Got it"
#      and show how many attempts it took them to get the correct number.
#   5. Let the player know the game is ending, or something that indicates the game is over.

# ( You can add more features/enhancements if you'd like to. )


# Kick off the program by calling the start_game function.

import random


def start_game() -> None:
    """
    Number Guessing Game function that allows a user to guess a number between 1 and 10 and lest them know
    how many attempts they took to guess the correct number generated randomly between 1 and 10
    """
    print("*" * 40)
    print("Welcome to the Number Guessing Game")
    print("*" * 40)
    user_guess: int
    num_of_tries: int = 1
    number_to_be_guessed: int = random.randint(1, 10)
    while True:
        try:
            user_guess: int = int(input("Guess a number between 1 and 10 : "))
            if user_guess < 1 or user_guess > 10:
                print("Please enter a number between 1 and 10")
                continue
            break
        except ValueError as e:
            print("Please enter a number between 1 and 10")
            continue

    while user_guess != number_to_be_guessed:
        if user_guess < number_to_be_guessed:
            print(f"It's higher than {user_guess}")
            user_guess = int(input("Guess a number between 1 and 10 : "))
            num_of_tries += 1
            continue
        else:
            print(f"It's lower than {user_guess}")
            user_guess = int(input("Guess a number between 1 and 10 : "))
            num_of_tries += 1
            continue
    stmt = f"Got it in {num_of_tries} attempt" if num_of_tries == 1 else f"Got it in {num_of_tries} attempts"
    print(stmt)
    print("Game is over, thanks for playing the number guessing game")


if __name__ == '__main__':
    start_game()
