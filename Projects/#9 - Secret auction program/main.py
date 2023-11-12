from presentation import welcome_message
from secret_auction import clear_console, get_name, get_bid, another_participant, find_max_bidder

print(welcome_message)
auction_dictionary = {}
while True:
    name = get_name()
    bid = get_bid(name)    
    auction_dictionary[name] = bid # This adds an entry to the auction_dictionary. The key of the entry is the participant's name (name), and the associated value is the bid entered by that participant (bid).
    if another_participant() == "no":
        break
    clear_console()    
max_bidder, max_bid = find_max_bidder(auction_dictionary) # Calls the function find_max_bidder(auction_dictionary) and assigns its returned values (the name of the highest bidder and the corresponding bid) to the variables max_bidder and max_bid using tuple unpacking. This line essentially extracts the results of the maximum bid calculation from the function and stores them in these variables for later use in the program.
print(f"The winner is {max_bidder} with a bid of ${max_bid}. Congratulations {max_bidder}!")
    
    


