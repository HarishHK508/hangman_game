import random

def choose_word():
    words = ['python', 'hangman', 'challenge', 'programming', 'developer']
    return random.choice(words)

def display_word(word, guessed_letters):
    return ' '.join([letter if letter in guessed_letters else '_' for letter in word])

def hangman_game():
    word = choose_word()
    guessed_letters = set()
    attempts_left = 6

    print("Welcome to Hangman!")
    
    while attempts_left > 0:
        print("\nWord:", display_word(word, guessed_letters))
        print("Guessed Letters:", ' '.join(sorted(guessed_letters)))
        print(f"Attempts Left: {attempts_left}")
        
        guess = input("Guess a letter: ").lower()

        if not guess.isalpha() or len(guess) != 1:
            print("Please enter a single alphabetic character.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.add(guess)

        if guess not in word:
            print("Wrong guess!")
            attempts_left -= 1

        if all(letter in guessed_letters for letter in word):
            print("\nCongratulations! You guessed the word:", word)
            break
    else:
        print("\nGame Over! The word was:", word)


hangman_game()
