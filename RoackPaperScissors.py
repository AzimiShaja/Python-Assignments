import random

# Define the valid choices
choices = ["rock", "paper", "scissors"]

# Ask the user for their choice
user_choice = input("Enter your choice (rock, paper, or scissors): ")

# Generate a random choice for the computer
computer_choice = random.choice(choices)

# Determine the winner
if user_choice == computer_choice:
    result = "Tie"
elif user_choice == "rock":
    if computer_choice == "paper":
        result = "Computer wins"
    else:
        result = "You win"
elif user_choice == "paper":
    if computer_choice == "scissors":
        result = "Computer wins"
    else:
        result = "You win"
else:
    if computer_choice == "rock":
        result = "Computer wins"
    else:
        result = "You win"

# Display the result to the user
print(
    f"You chose {user_choice}, and the computer chose {computer_choice}. {result}!")
