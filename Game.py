"""Number guessing game: guess a secret number between 1 and 100."""

import random

MIN_NUMBER = 1
MAX_NUMBER = 100


class GuessingGame:
    """Holds the secret number and counts the player's attempts."""

    def __init__(self, secret_number=None):
        if secret_number is None:
            secret_number = random.randint(MIN_NUMBER, MAX_NUMBER)
        self.secret_number = secret_number
        self.attempts = 0

    def check_guess(self, guess):
        """Count the attempt and return 'low', 'high' or 'correct'."""
        self.attempts += 1
        if guess < self.secret_number:
            return "low"
        if guess > self.secret_number:
            return "high"
        return "correct"


def read_guess():
    """Ask for a number until the player enters a valid one in range."""
    while True:
        try:
            guess = int(input(f"Enter a number from {MIN_NUMBER} to {MAX_NUMBER}: "))
        except ValueError:
            print("Please enter a valid whole number!")
            continue
        if MIN_NUMBER <= guess <= MAX_NUMBER:
            return guess
        print(f"The number must be between {MIN_NUMBER} and {MAX_NUMBER}.")


def main():
    game = GuessingGame()
    print("Welcome to the guessing game!")
    while True:
        result = game.check_guess(read_guess())
        if result == "low":
            print("Too low, try a higher number.")
        elif result == "high":
            print("Too high, try a lower number.")
        else:
            print(f"Congrats! You guessed the number in {game.attempts} attempts.")
            break


if __name__ == "__main__":
    main()
