import random

# Create a list of 5 favourite fruit
word_list = ["apple", "banana", "cherry", "strawberry", "peach"]

# Print out a random word from the list using the random.choice method
# Assignt he randomly selected word as word
word = random.choice(word_list)

# Print out this randomly selected word
print(word)

# Asking the user to input a single letter of the word and assigning it as the variable guess
guess = input("Enter a letter:" )

# Creating an if statement if a single letter is input and if it is in the word
if len(guess) == 1 and guess.isalpha():
    # If the letter is in the the word the followign message is printed
    print("Good guess!")
else:
    # If the letter is not in the word or more than 1 letter is input or if a number is input then the following is printed.
    print("Oops! That is an invalid input.")