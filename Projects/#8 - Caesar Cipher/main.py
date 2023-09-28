from presentation import welcome_message
from caesar_cipher import caesar, get_text, get_direction, get_shift, continue_cipher

print(welcome_message)  
while True: 
    text = get_text()
    shift = get_shift()
    direction = get_direction()
    caesar(text, shift, direction)    
    if not continue_cipher():
        break


    