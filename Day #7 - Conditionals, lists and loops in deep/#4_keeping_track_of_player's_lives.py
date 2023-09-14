import random

# STEP 4:

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
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
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

print('''
====================================      
      
Welcome to the Hangman game!

====================================

- Your main job is to guess the word. 
- If the guessed letter is in the word, it's revealed; if not, part of a hangman figure is drawn. 
- The guessing player continues until they guess the word or complete the hangman figure. 
- The game ends when the word is guessed correctly or when the hangman is completed, resulting in a loss. 
- You have up to 6 attempts. Good luck!''')
print(stages[6])

# Randomly choose a word from the word_list and assign it to a variable called chosen_word.
word_list = ["golosina", "huevo", "pollo", "ropx", "hauntzker", "vampi"]
chosen_word = random.choice(word_list)

# Create a variable to store the length of the 'chosen_word' variable and use it in for loops
word_length = len(chosen_word)

# Create a variable to store the length of the 'stages' variable and use it in for loops
stages_length = len(stages)

# Create a variable called 'lives' to keep track of the number of lives left. 
# Set 'lives' to equal 6.
lives = 6

# Create an empty list called display.
display = []

# For each letter in the chosen_word, add a "_" to 'display'.
# So if the chosen_word was "apple", display should be ["_", "_", "_", "_", "_"] with 5 "_" representing each letter to guess.
for letter in range(word_length):
    display += "_"
    
# Use a while loop to let the user guess again. 
# The loop should only stop once the user has guessed all the letters in the chosen_word and 'display' has no more blanks ("_"). 
# Then you can tell the user they've won.
while "_" in display:
    
    # Ask the user to guess a letter and assign their answer to a variable called guessed_letter. Make guessed_letter lowercase.
    guessed_letter = input("Please, guess a letter: ").lower()
    print(f"Guessed letter: {guessed_letter}")
    
    # Variable to track if a match was found.
    match_found = False
    
    # Loop through each position in the chosen_word;
    # If the letter at that position matches 'guessed_letter' then reveal that letter in the display at that position.
    # e.g. If the user guessed "p" and the chosen word was "apple", then display should be ["_", "p", "p", "_", "_"].
    for i in range(word_length):
        if chosen_word[i] == guessed_letter:
            display[i] = guessed_letter
            match_found = True
            print(display)
            
    # If guess is not a letter in the chosen_word, then reduce 'lives' by 1.
    if not match_found:
      lives -= 1
      print(f"You have {lives} lives left!")
      
      # Lives represents the remaining lives count and can be used as an index to access the corresponding state in the stages list.
      if lives >= 0 and lives < stages_length:
        print(stages[lives])
    
    # If lives goes down to 0 then the game should stop and it should print "You lose."
    if lives == 0:
      print("You've lost. Hangman was hanged!")
      break

# Print 'display' and you should see the guessed letter in the correct position and every other letter replace with "_".
if "_" not in display:
    print(f"Congratulations. You 've won!\nThe word is: {''.join(display).capitalize()}")
    # Join is used to concatenate a list into a single string.
    # Capitalize is used to capitalize the first letter of a string.



