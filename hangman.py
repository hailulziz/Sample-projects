import random
from words import words
import string

#get a random word from the words array in the words.py file
def get_valid_word(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)

    return word


def hangman():
    word = get_valid_word(words)
    word_letters = set(word) #convert the word string to a set
    alphabet = set(string.ascii_lowercase) #returns a set of all letters in the alphabet in uppercase
    used_letters = set()

    lives = 6

    while len(word_letters) > 0 and lives > 0: #while the set containing the letters of the word is not empty
        print('You have', lives, 'lives left and you have used these letters: ', ' '.join(used_letters))

         # what current word is (ie W - R D)
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('Current word: ', ' '.join(word_list))

        user_letter = input('Guess a letter: ').lower()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)

            else:
                lives = lives - 1
                print('Letter is not in word')

        elif user_letter in used_letters:
            print('\nYou have already used that letter. Guess another letter.')

        else:
            print('\nThat is not a valid letter.')

    if lives == 0:
        print('You died, sorry. The word was', word)
    else:
        print('You guessed the word', word, '!!')


hangman()
