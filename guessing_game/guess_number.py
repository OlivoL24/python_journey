import random

def guess_the_number():
  """Guess the number game.

  The computer generates a random number between 1 and 100, and the user has to guess it.

  Returns:
    True if the user guesses the number correctly, False otherwise.
  """

  # Generate a random number.
  number = random.randint(1, 100)

  # Get the user's guess.
  while True:
    try:
      guess = int(input("Guess a number between 1 and 100: "))
    except ValueError:
      print("Please enter an integer between 1 and 100.")
      continue

    # Check if the user guessed the number correctly.
    if guess == number:
      print("Congratulations! You guessed the number correctly!")
      return True
    elif guess < number:
      print("Your guess is too low.")
    else:
      print("Your guess is too high.")



if __name__ == "__main__":
  # Play the game until the user guesses the number correctly.
  while not guess_the_number():
    pass