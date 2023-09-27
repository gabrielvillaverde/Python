from presentation import welcome_message
from caesar_cipher import caesar, get_text, get_direction, get_shift, continue_cipher

# Calling the inputs for the user
while True:
    print(welcome_message)   
    text = get_text()
    shift = get_shift()
    direction = get_direction()
    caesar(text, shift, direction)    
    if not continue_cipher():
        break
    
# Bugs:

# Cuando inserto números, símbolos y espacios en el mensaje no funciona el código.
# Idear una forma que permita mantener números, símbolos y espacios. El resto de caracteres alfabéticos encriptarlos.

    