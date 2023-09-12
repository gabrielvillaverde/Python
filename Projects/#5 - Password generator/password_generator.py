import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))

# Easy Level - Order not randomised:
# e.g. 4 letter, 2 symbol, 2 number = JduE&!91

# Generating the character part of the password:
pw_with_letters = ""
for character in range(0, nr_letters):
    pw_with_letters += random.choice(letters)

# Generating the number part of the password:
pw_with_numbers = ""
for number in range(0, nr_numbers):
    pw_with_numbers += random.choice(numbers)

# Generating the symbol part of the password:
pw_with_symbols = ""
for symbol in range(0, nr_symbols):
    pw_with_symbols += random.choice(symbols)

# Concatenating the parts into a complete standard password:
password = pw_with_letters + pw_with_numbers + pw_with_symbols
print(password)

# Hard Level - Order of characters randomised:
# e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

# Convert the password (which is a string) into a list, and then store it in the variable my_list.
my_list = list(password)

# Shuffle the characters in the list since random.shuffle doesn't work with strings, only with lists.
random.shuffle(my_list)

# Concatenate a list of strings into a single string using join function.
random_password = "".join(my_list)

# Print the random password.
print(random_password)




