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


