import random

HANGMAN_PICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']


def get_random_word(filename="words.txt"):
    with open(filename, 'r') as f:
        words = f.read().splitlines()
    return random.choice(words)

def display_board(HANGMAN_PICS, missed_letters, correct_letters, secret_word):
    print(HANGMAN_PICS[len(missed_letters)])
    print()

    print('Missed letters:', end=' ')
    for letter in missed_letters:
        print(letter, end=' ')
    print()

    blanks = '_' * len(secret_word)

    for i in range(len(secret_word)): 
        if secret_word[i] in correct_letters:
            blanks = blanks[:i] + secret_word[i] + blanks[i+1:]

    print(' '.join(blanks))
    
def get_guess(already_guessed):
    while True:
        guess = input('Guess a letter or the full word: ').lower()
        if len(guess) != 1 and len(guess) != len(secret_word):
            print('Please enter a single letter or the full word.')
        elif guess in already_guessed:
            print('You already guessed that. Choose again.')
        elif not guess.isalpha():
            print('Please enter letters only.')
        else:
            return guess

def play_again():
    return input("Play again? (Yes/No): ").lower().startswith('y')
    

print('H A N G M A N')
name = input("Enter your name: ")
print(f"Hello {name}, let's play!")

missed_letters = ''
correct_letters = ''
secret_word = get_random_word('words.txt') 
game_is_done = False

while True:
    display_board(HANGMAN_PICS, missed_letters, correct_letters, secret_word)

    guess = get_guess(missed_letters + correct_letters)

    if guess == secret_word:
        print(f'Yes! The secret word is "{secret_word}"! You won!')
        game_is_done = True
    elif guess in secret_word:
        correct_letters += guess
    else:
        missed_letters += guess

    # Check if user won or lost
    if all(letter in correct_letters for letter in secret_word):
        print(f'Yes! The secret word is "{secret_word}"! You won!')
        game_is_done = True
    elif len(missed_letters) == len(HANGMAN_PICS) - 1:
        display_board(HANGMAN_PICS, missed_letters, correct_letters, secret_word)
        print(f'You ran out of guesses! The word was "{secret_word}".')
        game_is_done = True

    if game_is_done:
        if play_again():
            # Reset for a new game
            missed_letters = ''
            correct_letters = ''
            secret_word = get_random_word('words.txt') 
            game_is_done = False
        else:
            break 