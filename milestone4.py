import random

class Hangman:
    def __init__(self, word_list, num_lives = 5):
        self.word = self.get_random_word()
        self.word_guessed = ["_"]*len(self.word)
        self.num_letters = len(set(self.word))
        self.num_lives = num_lives
        self.word_list = word_list
        self.list_of_guesses = []
        
    def get_random_word(self):
        return random.choice(self.word_list)
    
    def check_guess(self):
        guess = guess.lower()
        if guess in self.word:
            print(f"Good guess! {guess} is in the word.")
            for letter in self.word:
                if letter == guess:
                    self.word_guessed[letter] = guess
            self.num_letters -= 1
        else:
            self.num_lives -= 1
            print(f"Sorry {guess} is no in the word.")
            print(f"You have {self.num_lives} left")
            
   
    def ask_for_input(self, guess):
        while True:
            guess = input("Enter a guess: ")
            if guess.isalpha() == False or len(guess) != 1:
                print("Invalid input. Please enter a single alphabetical letter.")
            elif guess in self.list_of_guesses:
                print("You have already tried this.")
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)
                break

hangman_game = Hangman(["apple", "pear", "strawberry"])
hangman_game.ask_for_input()
            

        
        


            
        

            
        

    





