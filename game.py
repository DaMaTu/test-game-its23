from hangman import *
from settings import *

game = Hangman()
settings = Settings()

missed_letters = ''
correct_letters = ''
secret_word = game.get_random_word('words.txt') 
game_is_done = False

while True:
    game.display_board(game.HANGMAN_PICS, missed_letters, correct_letters, secret_word)

    guess = game.get_guess(missed_letters + correct_letters, secret_word)

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
    elif len(missed_letters) == len(game.HANGMAN_PICS) - 1:
        game.display_board(game.HANGMAN_PICS, missed_letters, correct_letters, secret_word)
        print(f'You ran out of guesses! The word was "{secret_word}".')
        game_is_done = True

    if game_is_done:
        if game.play_again():
            # Reset for a new game
            missed_letters = ''
            correct_letters = ''
            secret_word = game.get_random_word('words.txt') 
            game_is_done = False
        else:
            break 