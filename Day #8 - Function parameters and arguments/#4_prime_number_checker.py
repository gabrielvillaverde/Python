# Prime numbers are numbers that can only be cleanly divided by themselves and 1.

# You need to write a function that checks whether if the number passed into it is a prime number or not.
# e.g. 2 is a prime number because it's only divisible by 1 and 2.
# But 4 is not a prime number because you can divide it by 1, 2 or 4.

# List of prime numbers (highlighted in yellow): https://cdn.fs.teachablecdn.com/NZqVclSt2qAe8KhTsUtw
    
def prime_checker(number):
    if number == 1:  # Special check for the number 1. By definition, prime numbers are greater than 1.
        print(f"{number} is not a prime number.")    
        return  # We exit the function using return; otherwise, the code would continue executing.
    
    is_prime = True  # Will change between true and false depending on whether the number is prime or not.
    for n in range(2, number):  # Loop in the range between 2 and the number entered by the user - 1.
        if number % n == 0:  # Checks if the division between the number entered by the user (number) and each number in the range (n) has a remainder of 0. If it finds any case, it will determine that there is more than one divisor. For example, 10 is divisible by 1, 2, 5, and 10; it is not prime.
             print(f"{number} is not a prime number, {n} is a divisor.")  # If it checks the number 10, it starts looping through the range between 2 and 10 and at first detects that 2 is a divisor of 10.
             is_prime = False  # Changes the flag to false and determines that it is not a prime number.
             break  # Breaks the loop and exits the iteration since it achieved its goal.
    
    if is_prime:
        print(f"{number} is a prime number.")

n = int(input("Check this number: "))
prime_checker(number=n)


    
