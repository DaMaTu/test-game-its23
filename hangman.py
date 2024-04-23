import random

class Hangman():
    def __init__(self):
        self.HANGMAN_PICS = ['''
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

    def get_random_word(self, filename="words.txt"):
        with open(filename, 'r') as f:
            words = f.read().splitlines()
        return random.choice(words)

    def display_board(self, HANGMAN_PICS, missed_letters, correct_letters, secret_word):
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
        
    def get_guess(self, already_guessed, secret_word):
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

    def play_again(self):
        return input("Play again? (Yes/No): ").lower().startswith('y')        
