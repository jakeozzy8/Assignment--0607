import random

#word choosing function w/ list of secret words
def choose_word():
    word_list = ["crane", "plumb", "frost", "night", "blaze", 
        "glove", "sword", "minty", "chalk", "brisk", "flung", "harps", "vowel",
        "quilt", "jumpy", "thumb", "dowry", "fixed", "laser", "bingo",
        "adieu", "audio", "stare", "house", "money","bread", 
        "light", "stone", "drink", "flame","black", "pride", "storm", 
        "dream", "bring", "march", "heart", "place", "shine", "world",
        "youth", "pilot", "bacon", "dwarf", "ghost", "tiger", "lunch", 
        "fresh", "waste", "pearl","chair", "slope", "crown", "knife", 
        "paint","gravy", "swing", "spice", "trade", "uncle",
        "wheat", "zebra", "mango", "lemon", "tulip", "robin", 
        "ocean", "angel", "daisy", "cloud",]

    secret_word = random.choice(word_list)
    return secret_word

#function for determining if the player guessed in 6 guesses or less
def has_won(player_input, secret_word):
    if player_input == secret_word:
        return True
    else:
        return False

#function for asking player for their word guess
def get_guess(previous_guesses):
    while True:
        player_input = input(str("Enter a five-letter word: ")).lower()
        if len(player_input) != 5:
            print("Your guess must be exactly 5 letters.")
        elif not player_input.isalpha():
            print("Your guess can only contain letters.")
        elif player_input in previous_guesses :
            print("You already guessed that word.")
        else:
            return player_input

#evaluates player guess and compares it to the secret word
def evaluate_guess(guess, secret_word):
    feedback = []
    for i in range(5):
        if guess[i] == secret_word[i]:
            feedback.append("G")
        elif guess[i] in secret_word:
            feedback.append("Y")
        else:
            feedback.append("-")
    return feedback

#displays the comparison of player guess vs secret word
def display_guess(guess, feedback):
    print("Guess: " + " ".join(guess.upper()))
    print("Feedback: " + " ".join(feedback))


