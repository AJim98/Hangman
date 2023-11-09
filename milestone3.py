word = "apple"

def check_guess():
    guess = input("Enter an letter: ")
    guess = guess.lower()
    if guess in word:
        print(f"Nice guess! {guess} is in the word!")
    else:
        print(f"Nice try, but {guess} isn't in the word. Try again")
    return guess

def ask_for_input():
    guess = check_guess()
    while True:
        if guess.isalpha():
            break
        else:
         print("Invalid input. Please enter a letter.")
         break
    return

ask_for_input()

