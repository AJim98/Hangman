def check_guess(self):
        guess = guess.lower()
        if guess in self.word:
            print(f"Good guess! {guess} is in the word.")
            for i,letter in self.word:
                if letter == guess:
                    self.word_guessed[i] = guess
            self.num_letters -= 1
        else:
            self.num_lives -= 1
            print(f"Sorry {guess} is no in the word.")
            print(f"You have {self.num_lives} left")
            
   
def ask_for_input(self, guess):
    while True:
        guess = input("Enter a guess: ").lower()
        if guess.isalpha() == False or len(guess) != 1:
            print("Invalid input. Please enter a single alphabetical letter.")
        elif guess in self.list_of_guesses:
            print("You have already tried this.")
        else:
            self.check_guess(guess)
            self.list_of_guesses.append(guess)
            break

ask_for_input()





#import random

#class Hangman:
#    def __init__(self, word_list, num_lives=5):
#        self.word_list = word_list
#        self.num_lives = num_lives
#        self.word = self.get_random_word()
#        self.word_guessed = ["_"] * len(self.word)
#        self.num_letters = len(set(self.word))
#        self.list_of_guesses = []
#
#    def get_random_word(self):
#        return random.choice(self.word_list)


