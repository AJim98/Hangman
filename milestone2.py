guess = input("Enter a letter:" )
if len(guess) == 1 and guess.isalpha():
    print("Good guess!")
else:
    print("Oops! That is an invalid input.")