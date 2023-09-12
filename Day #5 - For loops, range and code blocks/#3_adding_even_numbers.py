# Write a program that calculates the sum of all the even numbers from 1 to 100. Thus, the first even number would be 2 and the last one is 100:
# i.e. 2 + 4 + 6 + 8 + 10 ... + 98 + 100

# Important, there should only be 1 print statement in your console output. It should just print the final total and not every step of the calculation.

# Hint: there are quite a few ways of solving this problem, but you will need to use the range() function in any of the solutions.

# Solution using simple for and range function:

total_sum = 0
for number in range(0, 101, 2):
    total_sum += number    
print(total_sum)

# Solution using simple for, range function and conditionals. This is a more complex approach:

sum_of_evens = 0
for number in range(0, 101):  # Iterate from 0 to 100 (inclusive).
    if number % 2 == 0:  # Check if the number is even.
        sum_of_evens += number  # If it's even, add the number to the sum.
print(f"The sum of all even numbers in the range from 0 to 100 is: {sum_of_evens}")



