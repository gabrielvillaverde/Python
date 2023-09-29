# Creating my first dictionary
programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.", 
    "Function": "A piece of code that you can easily call over and over again."
    }

# Printing the dictionary
print(programming_dictionary)

# Printing only the first item of the dictionary
print(programming_dictionary["Bug"])

# Adding new items to the dictionary
programming_dictionary["Loop"] = "The action of doing something over and over again."

# Printing the dictionary with the new item
print(programming_dictionary)

# Creating and empty dictionary
new_dictionary = {}

# Adding new items to the empty dictionary
new_dictionary["River Plate"] = "The biggest club in Argentina."

# Printing the dictionary with the new item
print(new_dictionary)

# Wipe an existing dictionary
programming_dictionary = {}

# Printing the dictionary without any items, completely wiped out
print(programming_dictionary)

# Edit an item in a dictionary
new_dictionary["River Plate"] = "The biggest and most famous club in America."

# Printing the dictionary with the new edited item
print(new_dictionary)

# Loop through a dictionary and printing each item
for thing in new_dictionary: 
    print(thing) # This code only prints the keys, in this case: "River Plate"
    
# Loop through a dictionary and printing each item
for key in new_dictionary: 
    print(new_dictionary[key]) # This code prints the value of the key, in this case: "The biggest and most famous club in America."