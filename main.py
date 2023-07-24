from hangman_art import stages, logo
from hangman_words import word_list
import random

print(logo)

chosen_word = random.choice(word_list)
display_word = []
for letter in chosen_word:
    display_word += "_"

turns = 6

while turns > 0:
    guess = input("Guess a letter: ")
    if guess in display_word:
        print(f"You have already guessed {guess}.")
    for position in range(len(chosen_word)):
        if chosen_word[position] == guess:
            display_word[position] = guess
    if guess not in chosen_word:
        turns -= 1
        print(f"You have guessed {guess}. That is not in the word. You lose a life.")
    word_to_display = ""
    for letter in display_word:
        word_to_display += letter
    print(word_to_display)
    if turns > 0:
        print(stages[turns])

print(stages[0])
print(f"Game over, the word was {chosen_word}.")
