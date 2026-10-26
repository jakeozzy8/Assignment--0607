from wordle_functions import choose_word, get_guess, has_won, display_guess, evaluate_guess


#Welcome player to the game
print("Welcome to The Mystery Wordle! \n" \
"Your Goal is to guess the five letter word in 6 guesses or less!\n")
#Explain the rules
print("Guess the five-letter word. \n" \
"G = correct letter and position \n" \
"Y = correct letter, wrong position \n" \
"- = letter is not in the word\n \n")

#Each time through this loop is one full game
while True:
    #Set up a new game: pick a word and reset the guesses
    secret_word = choose_word()
    previous_guesses = []
    won = False

    #Give the player up to six attempts
    for attempt_count in range(1, 7):
        print("Attempt " + str(attempt_count) + " of 6")

        #Get a valid guess and remember it so it can't be reused
        guess = get_guess(previous_guesses)
        previous_guesses.append(guess)

        #Compare the guess to the secret word and show the result
        feedback = evaluate_guess(guess, secret_word)
        display_guess(guess, feedback)

        #End the game early if the player guessed the word
        if has_won(guess, secret_word):
            print("Congratulations! You solved the puzzle.")
            won = True
            break

    #If the player did not win, tell them and show the secret word
    if won == False:
        print("You didn't guess the word in 6 guesses!\n" \
        "The secret word was: " + secret_word + ".")

    #Ask if they want to play again, and stop this loop if they say no
    play_again = input("Would you like to play again? (Y/N) ").upper()
    if play_again != "Y":
        break
#Thank the player for playing
print("\nThank you for playing!")