# Write a program that will select a random name from a list of names. The person selected will have to pay for everybody's food bill.
# Important: You are not allowed to use the choice() function.
# Line 8 splits the string names_string into individual names and puts them inside a List called names. 
# For this to work, you must enter all the names as names followed by comma then space. e.g. "Angela, Ben, Jenny, Michael, Chloe"

import random

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

# Obtaining the list length
names_list_length = len(names)
print(f"List length: {names_list_length}.")

# Obtaining the random name
random_index = random.randint(0,names_list_length - 1)
print(f"Random index: {random_index}.")

# Obtaining the random name using the random index
random_name = names[random_index]
print(f"{random_name} is going to buy the meal today!")

# Alternative with random.choice()

random_choice = random.choice(names)
print(f"{random_name} is going to buy the meal today using random.choice() function!")







