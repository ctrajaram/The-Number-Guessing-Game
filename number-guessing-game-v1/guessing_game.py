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

high_score: any = None
lowest_num_tries: any = None


def start_game() -> None:
    """
    Number Guessing Game function that allows a user to guess a number between 1 and 10 and lest them know
    how many attempts they took to guess the correct number generated randomly between 1 and 10
    """
    global high_score, lowest_num_tries
    print("*" * 40)
    print("Welcome to the Number Guessing Game")
    print("*" * 40)
    user_guess: int = 0
    num_of_tries: int = 1
    play_again: str = 'NO'
    number_to_be_guessed: int = random.randint(1, 10)
    # Ensure the user has to enter a number between 1 and 10 to continue
    while True:
        try:
            user_guess: int = int(input("Guess a number between 1 and 10 : "))
            if user_guess < 1 or user_guess > 10:
                print("It is out of range so please enter a number between 1 and 10")
                continue
            break
        except ValueError as e:
            print("It is out of range so please enter a number between 1 and 10")
            continue

    while user_guess != number_to_be_guessed or play_again.upper() == 'YES':
        if user_guess < number_to_be_guessed:
            print(f"It's higher than {user_guess}")
            user_guess = int(input("Guess a number between 1 and 10 : "))
            num_of_tries += 1

            continue
        elif user_guess > number_to_be_guessed:
            print(f"It's lower than {user_guess}")
            user_guess = int(input("Guess a number between 1 and 10 : "))
            num_of_tries += 1
            continue

    stmt = f"Got it in {num_of_tries} attempt" if num_of_tries == 1 else f"Got it in {num_of_tries} attempts"
    if not lowest_num_tries:
        lowest_num_tries = num_of_tries
    if not high_score:
        high_score = num_of_tries
    high_score = num_of_tries if num_of_tries < high_score else high_score
    print(stmt)
    play_again = input("Do you want to play again type YES or NO: ")
    while play_again.upper() not in ('YES', 'NO'):
        play_again = input("Type YES to play another game or NO to exit the game: ")
    if play_again.upper() == 'NO':
        print("Game is over, thanks for playing the number guessing game")
    else:
        print(f"The high score or least number of guesses you need to beat is {high_score}")
        start_game()


# This statement checks if the current file is being run directly (not imported as a module). If it's running
# directly, the `__name__` variable will be set to `'__main__'`. This is often used to run test code or a main
# function (like `start_game()`) only when the script is executed directly, but not when the script is imported
# as a module in another script.
if __name__ == '__main__':
    start_game()
