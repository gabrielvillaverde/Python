import random
import hangman_words
import hangman_art

# Randomly choose a word from the word_list and assign it to a variable called chosen_word.
word_list = hangman_words.word_list
chosen_word = random.choice(word_list)

# Shows a welcome message
print(hangman_art.welcome_message)

# Create a variable to store the length of the 'chosen_word' variable and use it in for loops
word_length = len(chosen_word)

# Create a variable to store the length of the 'stages' variable and use it in for loops
stages_length = len(hangman_art.stages)

# Create a variable called 'lives' to keep track of the number of lives left. 
# Set 'lives' to equal 6.
lives = 6

# Create an empty list called display.
display = []

# Create an empty list to keep a record of guessed letters
guessed_letters = []

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
    
    # Checks if the letters has already been guessed
    if guessed_letter in guessed_letters:
        print(f"The letter '{guessed_letter}' has already been guessed. Please choose another one. Relax! You are not losing any lives. You still have {lives} remaining.\nHere's the result:\n{display}")
        continue  # Continue with the next loop iteration without processing the repeated letter.

    guessed_letters.append(guessed_letter)  # Adds the letter to guessed letters list.
    
    # Variable to track if a match was found.
    match_found = False
    
    # Loop through each position in the chosen_word;
    # If the letter at that position matches 'guessed_letter' then reveal that letter in the display at that position.
    # e.g. If the user guessed "p" and the chosen word was "apple", then display should be ["_", "p", "p", "_", "_"].
    for i in range(word_length):
        if chosen_word[i] == guessed_letter:
            display[i] = guessed_letter
            match_found = True
       
    # Print 'display' and you should see the guessed letter in the correct position and every other letter replace with "_".
    if match_found:
      print(f"Correct! The letter '{guessed_letter}' appears in the word.\nHere's the result:\n{display}\nAlready guessed letters: {', '.join(guessed_letters)}.")

            
    # If guess is not a letter in the chosen_word, then reduce 'lives' by 1.
    if not match_found:
      lives -= 1
      print(f"Incorrect! The letter '{guessed_letter}' does not appear in the word. You have {lives} lives left.\nHere's the result:\n{display}.")
      
      # Lives represents the remaining lives count and can be used as an index to access the corresponding state in the stages list.
      if lives >= 0 and lives < stages_length:
        print(f"{hangman_art.stages[lives]}\nAlready guessed letters: {', '.join(guessed_letters)}.")

    # If lives goes down to 0 then the game should stop and it should print "You lose."
    if lives == 0:
      print(f"You have lost. Hangman was hanged!\nThe word was {chosen_word.capitalize()}.")
      break

# Print 'display' and you should see the guessed letter in the correct position and every other letter replace with "_".
if "_" not in display:
    print(f"Congratulations. You have won!\nThe word is {''.join(display).capitalize()}")
    # Join is used to concatenate a list into a single string.
    # Capitalize is used to capitalize the first letter of a string.
