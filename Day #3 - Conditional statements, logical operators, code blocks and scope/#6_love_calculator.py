# Write a program that tests the compatibility between two people.
# To work out the love score between two people:
# Take both people's names and check for the number of times the letters in the word "TRUE" occurs. 
# Then check for the number of times the letters in the word "LOVE" occurs. 
# Then combine these numbers to make a 2 digit number.

print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

# Combine the names and convert the entire string to lowercase.
combined_names = name1.lower() + name2.lower()

# Count the occurrences of specific letters
t = combined_names.count("t")
r = combined_names.count("r")
u = combined_names.count("u")
e = combined_names.count("e")

l = combined_names.count("l")
o = combined_names.count("o")
v = combined_names.count("v")
e = combined_names.count("e")

true_appearances = t + r + u + e
love_appearances = l + o + v + e

result = str(true_appearances) + str(love_appearances)
result_as_int = int(result)

# For Love Scores less than 10 or greater than 90, the message should be:

if result_as_int <= 10 or result_as_int >= 90:
    print(f"Your score is {result_as_int}, you go together like coke and mentos.")

# For Love Scores between 40 and 50, the message should be:

elif result_as_int >= 40 and result_as_int <= 50:
    print(f"Your score is {result_as_int}, you are alright together.")
    
# Otherwise, the message will just be their score. e.g.:
else:
    print(f"Your score is {result_as_int}.")

    







