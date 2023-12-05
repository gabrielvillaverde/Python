import art

print(art.logo)

def add(a, b):
    """This function adds two numbers."""
    return a + b

def subtract(a, b):
    """This function subtracts b from a."""
    return a - b

def multiply(a, b):
    """This function multiplies two numbers."""
    return a * b

def divide(a, b):
    """This function divides a by b."""
    if b != 0:
        return a / b
    else:
        raise ValueError("Division by zero is undefined.")
    
dict_operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}
"""
This dictionary stores functions with possible operations that the user can perform (+ | - | * | /).
Each key represents an operator, and its corresponding value is the function to perform that operation.
"""

while True:
    try:
        num1 = float(input("Enter the first number: "))
        break
    except ValueError:
        print("Invalid input. Please enter a valid number.")

while True:
    operation_symbol = input("Enter the desired operation: add (+), subtract (-), multiply (*) or divide (/). Please type only symbols: ")
    if operation_symbol in dict_operations:
        break
    else:
        print("Invalid input. Please enter a valid operation symbol.")

while True:
    try:
        num2 = float(input("Enter the second number: "))
        break 
    except ValueError:
        print("Invalid input. Please enter a valid number.")
print("You entered valid numbers and operation:", num1, operation_symbol, num2)

calculation_function = dict_operations[operation_symbol] # This line retrieves the corresponding calculation function based on the user's input symbol (operation_symbol) from the dict_operations dictionary.
result = calculation_function(num1, num2) # The selected calculation function is then called with the user's input numbers (num1 and num2), and the result is stored in the variable result.
print(f"The result of {num1} {operation_symbol} {num2} is: {result}")

while True:
    user_answer = input("Do you wish to continue performing calculations? Type 'y' or 'yes' to keep going, otherwise type 'n' or 'no' to exit. ")
    if user_answer.lower() in ['y', 'yes']:       
         
        while True:
            operation_symbol = input("Continue with another operation. Please, remember to enter the desired operation: add (+), subtract (-), multiply (*) or divide (/). Please type only symbols: ")
            if operation_symbol in dict_operations:
                break
            else:
                print("Invalid input. Please enter a valid operation symbol.")
                
        while True:
            try:
                num3 = float(input("Enter the new number: "))
                break 
            except ValueError:
                print("Invalid input. Please enter a valid number.")
        print("You entered valid numbers and operation:", result, operation_symbol, num3)

        calculation_function = dict_operations[operation_symbol] 
        result = calculation_function(result, num3)
        print(f"The result of {result} {operation_symbol} {num3} is: {result}") # ACA TA EL ERROR, NOSE DONDE UBICARLO
        
    elif user_answer.lower() in ['n', 'no']:
        print(f"The final result is: {result}")
        break
    else:
        print("Invalid input. Type 'y' or 'yes' to keep going, otherwise type 'n' or 'no' to exit.")
        
# BUG: el codigo funca bien, los resultados estan bien, pero el print ta mal, ponele si haces 200 + 200 en la primera operación te da 400, y si le restas 100 te da 300. ta ok, pero el print dice 300 - 100: 300, debería decir 400 - 100.