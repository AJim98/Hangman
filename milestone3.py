import random

word_list = ["Apple", "Banana", "Cherry", "Strawberry", "Peach"]
word = random.choice(word_list)

def check_guess(guess):
    guess = guess.lower()
    if guess in word.lower():
        print(f"Nice guess! {guess} is in the word!")
    else:
        print(f"Nice try, but {guess} isn't in the word. Try again")

def ask_for_input():
    while True:
        guess = input("Enter an letter: ")
        if len(guess) == 1 and guess.isalpha():
            print("Good guess!")
            check_guess(guess)
        else:
            print("Invalid input. Please enter a single alpabetical character.")

ask_for_input()