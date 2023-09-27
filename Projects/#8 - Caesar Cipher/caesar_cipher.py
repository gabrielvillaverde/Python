alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    
def caesar(message, movements_amount, direction):
    final_message = ""
    for char in message:
        position = alphabet.index(char)
        if direction == 'encode':
            new_position = (position + movements_amount) % 26
            decrypted_char = alphabet[new_position]
            final_message += decrypted_char
        elif direction == 'decode':
            new_position = (position - movements_amount) % 26
            decrypted_char = alphabet[new_position]
            final_message += decrypted_char
    print(f"The original message is: {message}\nThe {direction} message is: {final_message}")
    
def get_text():
    while True:
        text = input("Type your message: ").lower()
        return text
        
def get_shift():
    while True:
        try:
            shift = int(input("Type the shift number: "))
            return shift
        except ValueError:
            print("Please enter a valid integer for the shift.")
    
def get_direction():
    while True:
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: ").lower()
        if direction == 'encode' or direction == 'decode':
            return direction
        else:
            print("Please enter 'encode' or 'decode'.")
    
def continue_cipher():
    while True:
        choice = input("Do you want to continue? yes/no ").lower()
        if choice == 'yes':
            return True
        elif choice == 'no':
            return False
        else:
            print("Please, enter 'yes' or 'no'.")
