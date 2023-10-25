from presentation import welcome_message
from secret_auction import clear_console

print(welcome_message)

auction_dictionary = {}

while True:
    while True:
        name = input("What is your name? ")
        if name.isalpha():
            name = name.capitalize()
            break
        else:
            print("Please enter alphabetic characters only for your name.")
    
    while True:
        bid_input = input(f"Hello {name}, what is your bid? ")
        try:
            bid = int(bid_input)
            break
        except ValueError:
            print("Please enter only numbers for the bid.")

    auction_dictionary[name] = bid

    while True:
        another_participant = input("Is there another participant? Type 'yes' or 'no' ").lower()
        if another_participant == "yes" or another_participant == "no":
            break
        else:
            print("Please type 'yes' or 'no'.")

    if another_participant == "no":
        break
    clear_console()
    
max_bidder = max(auction_dictionary, key=auction_dictionary.get)
max_bid = auction_dictionary[max_bidder]

print(f"The winner is {max_bidder} with a bid of ${max_bid}. Congratulations {max_bidder}!")

# THINGS TO IMPROVE: CREATE FUNCTIONS OF THE INPUTS OF NAME AND BID, ALL IN ONE
    
    


