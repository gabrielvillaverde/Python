import random

# STEP 1:

# Randomly choose a word from the word_list and assign it to a variable called chosen_word.
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
print(f"Chosen word: {chosen_word}")

# Ask the user to guess a letter and assign their answer to a variable called guessed_letter. Make guessed_letter lowercase.
guessed_letter = input("Please, guess a letter: ").lower()
print(f"Guessed letter: {guessed_letter}")

# Check if the letter the user guessed (guessed_letter) is one of the letters in the chosen_word.
letter_counter = 0
letter_found = False # Variable to track if at least one match is found.

for letter in chosen_word:
    if guessed_letter == letter:
        letter_counter += 1
        letter_found = True # A match is found, change the variable to True.

if letter_found:
    print(f"The letter '{guessed_letter}' appears {letter_counter} times in {chosen_word}")
else:
    print(f"The letter '{guessed_letter}' does not appear in {chosen_word}")
