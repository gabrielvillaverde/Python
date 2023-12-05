import functions
import art

dict_operations = {
    "+": functions.add,
    "-": functions.subtract,
    "*": functions.multiply,
    "/": functions.divide
}
"""
This dictionary stores functions with possible operations that the user can perform (+ | - | * | /).
Each key represents an operator, and its corresponding value is the function to perform that operation.
"""

def calculator():
  print(art.logo)

  num1 = float(input("What's the first number?: "))
  for symbol in dict_operations:
    print(symbol)
  should_continue = True
 
  while should_continue:
    operation_symbol = input("Pick an operation: ")
    num2 = float(input("What's the next number?: "))
    calculation_function = dict_operations[operation_symbol]
    answer = calculation_function(num1, num2)
    print(f"{num1} {operation_symbol} {num2} = {answer}")

    if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ") == 'y':
      num1 = answer
    else:
      should_continue = False
      calculator()

calculator()
