import random
import sys

def random_number():
    return random.randint(1, 100)

def guess_the_number():
    """Guess the number game.

    The computer generates a random number between 1 and 100, and the user has to guess it.

    Returns:
        True if the user guesses the number correctly, False otherwise.
    """

    # Generate a random number.
    number = random_number()

    # initialize guess counter
    guess_count = 0
    # Get the user's guess.
    while True:
    # Get the user's guess.
        guess = input("Guess a number between 1 and 100: ")

        # Check if the user wants to quit.
        if guess == "q":
            print("You have quit the game.")
            sys.exit()

        # Check if the user's guess is correct.
        try:
            guess = int(guess)
        except ValueError:
            print("Please enter an integer between 1 and 100.")
            continue

        if guess == number:
            print("Correct! You guessed the number in {} guesses!".format(guess_count))
            play_again = input("Do you want to play again? (y/n): ")
            if play_again == "y":
                number = random_number()
                guess_count = 0
                continue
            else:
                sys.exit()

        if guess < number:
            print("Your guess is too low.")
        else:
            print("Your guess is too high.")
        guess_count += 1
        



if __name__ == "__main__":
  # Play the game until the user guesses the number correctly.
  while not guess_the_number():
    pass