import presentation

# Shows a welcome message
print(presentation.welcome_message)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

# First task: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.

def encrypt(message, movements):

# Second task: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.  
# e.g. 
# plain_text = "hello"
# shift = 5
# cipher_text = "mjqqt"
# print output: "The encoded text is mjqqt"

    encrypted_text = ""
    for char in message:
        index = alphabet.index(char)
        new_index = index + movements
        encrypted_char = alphabet[new_index]
        encrypted_text += encrypted_char
        #🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛
    print(encrypted_text)

# Third task: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message.
if direction == "encode":
    encrypt(text, shift)