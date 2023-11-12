from presentation import welcome_message
from secret_auction import clear_console, get_name, get_bid, another_participant

print(welcome_message)

auction_dictionary = {}

while True:
    name = get_name()
    bid = get_bid(name)
        
    auction_dictionary[name] = bid

    if another_participant() == "no":
        break
    clear_console()
    
max_bidder = max(auction_dictionary, key=auction_dictionary.get) # This line uses the max() function to find the key (participant's name) that has the maximum value in the auction_dictionary dictionary. The key=auction_dictionary.get part instructs max() to use the values of the dictionary to determine the maximum.
max_bid = auction_dictionary[max_bidder]

print(f"The winner is {max_bidder} with a bid of ${max_bid}. Congratulations {max_bidder}!")
    
    


