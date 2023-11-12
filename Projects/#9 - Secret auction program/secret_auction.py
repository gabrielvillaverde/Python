# The function clear_console() uses the os library to interact with the operating system and execute a specific command to clear the console screen.
# The expression 'cls' if os.name == 'nt' else 'clear' is a ternary operator. 
# On Windows operating systems, the command to clear the console is cls, while on Unix-based systems (such as Linux and macOS), the command is clear. 
# Therefore, this expression selects the appropriate command based on the operating system on which the program is running.

import os

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')
    
# ----------------------------------------------------------------------------------- #
    
def get_name():
    while True:
        name = input("What is your name? ")
        if name.isalpha():
            name = name.capitalize()
            return name
        else:
            print("Please enter alphabetic characters only for your name.")
    
def get_bid(name):
    while True:
        bid_input = input(f"Hello {name}, what is your bid? ")
        try:
            bid = int(bid_input)
            return bid
        except ValueError:
            print("Please enter only numbers for the bid.")
            
def another_participant():
    while True:
        answer = input("Is there another participant? Type 'yes' or 'no' ").lower()
        if answer == "yes" or answer == "no":
            return answer
        else:
            print("Please type 'yes' or 'no'.")
            
def find_max_bidder(auction_dictionary):
    max_bidder = max(auction_dictionary, key=auction_dictionary.get)
    max_bid = auction_dictionary[max_bidder]
    return max_bidder, max_bid

    
    
    
