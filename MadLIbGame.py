# Ask the user for a series of words
name = input("Enter a name: ")
adjective1 = input("Enter an adjective: ")
adjective2 = input("Enter another adjective: ")
noun1 = input("Enter a noun: ")
noun2 = input("Enter another noun: ")
verb = input("Enter a verb: ")
animal = input("Enter an animal: ")
food = input("Enter a food: ")
fruit = input("Enter a fruit: ")
superhero = input("Enter a superhero name: ")
country = input("Enter a country: ")
dessert = input("Enter a dessert: ")
year = input("Enter a year: ")

# Fill in the blanks of the story with the user's words
story = f"{name} was a {adjective1} {noun1} who dreamed of becoming a {adjective2} {noun2}. One day, {name} decided to {verb} with a {animal} to get closer to nature. While exploring the wilderness, {name} stumbled upon a secret cave full of {food} and {fruit}. Little did {name} know, this was the hiding place of the evil {superhero} who had been banished from {country} for his love of {dessert}. {name} knew he had to stop {superhero} before he could cause any more chaos. With the help of a wise {animal}, {name} defeated {superhero} and saved the world from destruction in the year {year}."

# Display the story to the user
print(story)
