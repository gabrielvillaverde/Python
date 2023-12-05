import art

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
    
def calculator(dict_operations):
    """This function encompasses the entire calculation process, user inputs, data validations, and internal operation of the calculator.
       The function receives dict_operations as a parameter to avoid circular references and eliminate the need to import the main.py module into the functions.py module. 
       This enables functions.py to operate independently and adapt to different dictionaries without relying on a specific module. 
       Now, functions.py can be used in other projects."""
    print(art.logo)
    should_continue = True
    first_number = 0  # Initialize first_number out of the main loop
    while should_continue:
        try:
            if first_number == 0:
                first_number = float(input("Enter the first number: "))
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            continue
        while True:
            operation_symbol = input("Enter the desired operation: add (+), subtract (-), multiply (*) or divide (/). Please type only symbols: ")
            if operation_symbol in dict_operations:
                break
            else:
                print("Invalid input. Please enter a valid operation symbol.")
        while True:
            try:
                next_number = float(input("Enter the next number: "))
                break 
            except ValueError:
                print("Invalid input. Please enter a valid number.")

        print("You entered valid numbers and operation:", first_number, operation_symbol, next_number)

        calculation_function = dict_operations[operation_symbol]
        result = calculation_function(first_number, next_number)
        print(f"The result of {first_number} {operation_symbol} {next_number} is: {result}")

        while True:
            user_answer = input("Do you wish to continue performing calculations?\n - Type 'y' or 'yes' to keep going.\n - Type 'n' or 'no' to exit the calculator.\n - Type 'new' if you want to perform a new calculation. ")
            if user_answer.lower() in ['y', 'yes']:       
                first_number = result
                print(art.logo)
                print(f"Your currently result is: {result}")    
                break
            elif user_answer.lower() in ['n', 'no']:
                print(f"The final result is: {result}")
                should_continue = False
                break
            elif user_answer.lower() == 'new':
                print(art.logo)
                first_number = 0  # Restart first_number if the user choose 'new'. This feature ensures that first_number retains its value between iterations unless the user chooses to initiate a new operation (new), in which case it is reset to zero.
                break
            else:
                print("Invalid input. Type 'y' or 'yes' to keep going, type 'n' or 'no' to exit, or type 'new' to perform a new calculation.")
