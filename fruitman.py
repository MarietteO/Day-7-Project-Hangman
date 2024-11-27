from art import stages
import random
import string

alphabet = string.ascii_lowercase
alphabet_list = list(alphabet)
word_list = ["apple", "pear", "orange", "banana", "blueberry", "lemon", "plum",
             "pineapple", "strawberry", "kiwifruit", "raspberry", "tomato", "dragonfruit", "durian",
             "apricot", "peach", "grapefruit", "lime", "tangerine", "blackcurrant", "pomegranate",
             "watermelon", "melon", "cranberry", "grape", "guava", "lychee"]


def check_answer(hidden_word, secret_word, turns):
    while True:
        if turns > -1:
            if "_" in hidden_word:
                guess = input("Guess a letter: ").lower()
                if guess.isalpha():
                    if len(guess) != 1:
                        print("Only one letter at a time, please.")
                    elif guess not in secret_word:
                        print("That letter is not in the word.")
                        print(stages[turns])
                        turns -= 1
                    else:
                        hidden_word_list = list(hidden_word)
                        position = -1
                        for letter in secret_word:
                            position += 1
                            if letter == guess:
                                hidden_word_list[position] = secret_word[position]
                                hidden_word = "".join(hidden_word_list)
                        print(hidden_word)
            else:
                print("Congratulations! You have saved the Fruitman.")
                break
        else:
            print("Your guesses are done, and so is the Fruitman.")
            break


sec_word = random.choice(word_list)
hid_word = ""
for _ in sec_word:
    hid_word += "_"

guesses = 6

print("Welcome to Fruitman. The Fruitman's fate is in your hands. \nThe secret word is a fruit or a berry. "
      "Guess the secret word: ")
print(hid_word)
print(f"(Psst, the secret word is {sec_word}.)")
check_answer(hid_word, sec_word, guesses)
