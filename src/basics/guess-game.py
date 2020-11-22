#User to interact with the program until they get our hidden/secret word correct
secret_word = "Gichure"
guess = ""
guess_count = 0
guess_limit = 5;
out_of_guesses = False

while guess != secret_word and not(out_of_guesses):
    if(guess_count < guess_limit):
        guess = input("Enter your guess word: ")
        guess_count += 1
    else:
        out_of_guesses = True
if out_of_guesses:
    print("You lose the game")
else:
    print("You got it correct after "+str(guess_count) + "times")