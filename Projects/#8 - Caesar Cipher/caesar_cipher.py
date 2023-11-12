alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    
def caesar(message, movements_amount, direction):
    final_message = ""
    for char in message:
        if char.isalpha():
            position = alphabet.index(char)
            if direction == 'encode':
                # I use the modulo operator to obtain the remainder of the division between the number of shifts and the 26 letters of the alphabet. 
                # This remainder will dynamically adjust according to the number of shifts we input and prevent overflow.
                new_position = (position + movements_amount) % 26
                decrypted_char = alphabet[new_position]
                final_message += decrypted_char
            elif direction == 'decode':
                new_position = (position - movements_amount) % 26
                decrypted_char = alphabet[new_position]
                final_message += decrypted_char
        else:
            final_message += char
    print(f"\nThe original message is: {message}\nThe {direction} message is: {final_message}")
    
def get_text():
    while True:
        text = input("\nType your message: ").lower()
        return text
        
def get_shift():
    while True:
        try:
            shift = int(input("\nType your secret number: "))
            return shift
        except ValueError:
            print("\nPlease enter a valid integer for the shift.")
    
def get_direction():
    while True:
        direction = input("\nType 'encode' to encrypt, type 'decode' to decrypt: ").lower()
        if direction == 'encode' or direction == 'decode':
            return direction
        else:
            print("\nPlease enter 'encode' or 'decode'.")
    
def continue_cipher():
    while True:
        choice = input("\nDo you want to continue? yes/no ").lower()
        if choice == 'yes':
            return True
        elif choice == 'no':
            print("\nThank you for using Caesar Cipher! Goodbye!")
            return False
        else:
            print("\nPlease, enter 'yes' or 'no'.")