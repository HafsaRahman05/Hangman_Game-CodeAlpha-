import random
# ASCII Hangman states
HANGMAN_PICS = [
    """
     +---+
         |
         |
         |
        ===""",
    """
     +---+
     O   |
         |
         |
        ===""",
    """
     +---+
     O   |
     |   |
         |
        ===""",
    """
     +---+
     O   |
    /|   |
         |
        ===""",
    """
     +---+
     O   |
    /|\\  |
         |
        ===""",
    """
     +---+
     O   |
    /|\\  |
    /    |
        ===""",
    """
     +---+
     O   |
    /|\\  |
    / \\  |
        ==="""
]

# Word lists by difficulty
WORD_LISTS = {
    "easy": ["apple", "book", "cake", "dog", "fish"],
    "medium": ["banana", "orange", "grapes", "planet", "python"],
    "hard": ["dolphin", "hangman", "puzzling", "Enhancement", "Congratulations"]
}

def choose_word(difficulty):
    return random.choice(WORD_LISTS[difficulty])

def print_game_state(display_word, guessed_letters, wrong_guesses, max_wrong_guesses):
    print(HANGMAN_PICS[wrong_guesses])
    print(f"\nWord: {' '.join(display_word)}")
    print(f"Wrong guesses: {wrong_guesses}/{max_wrong_guesses}")
    print(f"Guessed letters: {', '.join(sorted(guessed_letters))}\n")

def play_single_round():
    # Difficulty selection
    while True:
        difficulty = input("\n Choose difficulty (easy/medium/hard): ").lower()
        if difficulty in WORD_LISTS:
            break
        print("Invalid difficulty. Choose from easy, medium, or hard.\n")

    word_to_guess = choose_word(difficulty)
    display_word = ["_" for _ in word_to_guess]
    guessed_letters = set()
    wrong_guesses = 0
    max_wrong_guesses = len(HANGMAN_PICS) - 1
    hint_used = False

    print("\nGame Start!\n")

    while wrong_guesses < max_wrong_guesses and "_" in display_word:
        print_game_state(display_word, guessed_letters, wrong_guesses, max_wrong_guesses)
        
        guess = input("Guess a letter or type 'hint': ").lower()

        if guess == "hint":
            if hint_used:
                print("Hint already used!\n")
                continue
            hint_letter = random.choice([c for c in word_to_guess if c not in guessed_letters])
            print(f"Hint: Try guessing '{hint_letter}'\n")
            hint_used = True
            continue

        if not guess.isalpha() or len(guess) != 1:
            print("Invalid input. Enter a single alphabetical character.\n")
            continue

        if guess in guessed_letters:
            print("You've already guessed that letter. Try another one.\n")
            continue

        guessed_letters.add(guess)

        if guess in word_to_guess:
            print(f"✅ Good job! '{guess}' is in the word.\n")
            for i, letter in enumerate(word_to_guess):
                if letter == guess:
                    display_word[i] = guess
        else:
            print(f"❌ Oops! '{guess}' is not in the word.\n")
            wrong_guesses += 1

    print_game_state(display_word, guessed_letters, wrong_guesses, max_wrong_guesses)

    if "_" not in display_word:
        print(f"🎉 Congratulations! You guessed the word: {word_to_guess}\n")
    else:
        print(f"💀 Game over! The word was: {word_to_guess}\n")

def play_hangman():
    print("🎮 Welcome to Advanced Hangman 🎮")
    while True:
        play_single_round()
        again = input("Do you want to play again? (yes/no): ").strip().lower()
        if again not in ("yes", "y"):
            print("\n🙏 Thanks for playing! See you next time.\n")
            break

# Start the game
if __name__ == "__main__":
    play_hangman()
