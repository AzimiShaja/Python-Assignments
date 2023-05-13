import random

# Generate a random number between 1 and 100
number = random.randint(1, 100)

# Initialize the number of guesses
guesses = 0

# Ask the user to guess the number
while True:
    guess = int(input("Guess the number (between 1 and 100): "))
    guesses += 1

    # Check if the guess is correct
    if guess == number:
        print(f"Congratulations! You guessed the number in {guesses} guesses.")
        break
    # If the guess is too high or too low, give a hint
    elif guess < number:
        print("Too low. Try again.")
    else:
        print("Too high. Try again.")
