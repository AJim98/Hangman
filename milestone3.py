word = "apple"
while True:
    guess = input("Enter an letter: ")
    if guess.isalpha():
        break
    else:
        print("Invalid input. Please enter a letter.")
    

if guess in word:
    print(f"Nice guess! {guess} is in the word!")
else:
    print(f"Nice try, but {guess} isn't in the word. Try again")
