import os

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')
    
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

    
    
    
