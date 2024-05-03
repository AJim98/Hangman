import random

# Creating the Hangman Class
class Hangman:
    def __init__(self, word_list, num_lives = 5): 
        # Creating the magic method for the Hangman class.
        self.word = random.choice(word_list)
        self.word_guessed = ["_" for _ in range(len(self.word))]
        self.num_letters = len(self.word)
        self.num_lives = num_lives
        self.word_list = word_list
        self.list_of_guesses = []
        
    def check_guess(self, guess):
        # This checks to see if the input letter is in the randomly selected word and then updated the game as needed.
        guess = guess.lower()
        if guess in self.word.lower():
            print(f"Good guess! {guess} is in the word.")
            for i, letter in enumerate(self.word):
                if self.word.lower()[i] == guess:
                    self.word_guessed[i] = guess
            print(self.word_guessed)
            self.num_letters -= 1
        else:
            if guess not in self.list_of_guesses:
                self.list_of_guesses.append(guess)   # If the guess is not in the word, add it to the list of guessed words.
                self.num_lives -= 1
                print(f"Sorry but {guess} is not in the word. Please try again.")
                if self.num_lives >= 1:
                    print(f"You have {self.num_lives} left.")
                else:
                    self.num_lives == 0
                    print(f"You have {self.num_lives}.Game over!")
            
    def ask_for_input(self):
        while True:
            guess = input("Enter a guess: ")
            if guess.isalpha() == False or len(guess) != 1:
                print("Invalid input. Please enter a single alphabetical letter.")
            elif guess in self.list_of_guesses:
                print("You have already tried this letter!")
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)
    
# This block of code is used to play the game.
def play_game(word_list):
    num_lives = 5
    game = Hangman(word_list, num_lives)
    while True:
        if game.num_lives == 0:
            print(f"You have {game.num_lives} lives, you have lost!")
            break
        elif game.num_lives > 0:
            game.ask_for_input()
        else:
            print("Congratulations, you have won!!!")
            break

# This is a conditional statement that tells python to run under certain conditions.
if __name__ == "__main__":
    word_list = ["Apple", "Banana", "Cherry", "Strawberry", "Peach"]
    play_game(word_list)