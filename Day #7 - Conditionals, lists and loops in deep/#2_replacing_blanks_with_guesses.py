import random

# STEP 2:

# Randomly choose a word from the word_list and assign it to a variable called chosen_word.
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
print(f"Chosen word: {chosen_word}")

# Create a variable to store the length of the 'chosen_word' variable and use it in for loops
word_length = len(chosen_word)

# Ask the user to guess a letter and assign their answer to a variable called guessed_letter. Make guessed_letter lowercase.
guessed_letter = input("Please, guess a letter: ").lower()
print(f"Guessed letter: {guessed_letter}")

# Create an empty list called display.
display = []

# For each letter in the chosen_word, add a "_" to 'display'.
# So if the chosen_word was "apple", display should be ["_", "_", "_", "_", "_"] with 5 "_" representing each letter to guess.
for letter in range(word_length):
    display += "_"
    
# Loop through each position in the chosen_word;
# If the letter at that position matches 'guessed_letter' then reveal that letter in the display at that position.
# e.g. If the user guessed "p" and the chosen word was "apple", then display should be ["_", "p", "p", "_", "_"].
match_found = False
for i in range(word_length):
    if chosen_word[i] == guessed_letter:
        display[i] = guessed_letter
        match_found = True

# Print 'display' and you should see the guessed letter in the correct position and every other letter replace with "_".
if match_found:
    print(display)
else:
    print(f"The letter '{guessed_letter}' does not appear in {chosen_word}")


