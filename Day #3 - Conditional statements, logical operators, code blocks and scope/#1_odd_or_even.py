# In this programming exercise, you'll be writing a simple program that checks whether a given integer is an odd or an even number.

number = int(input("Which number do you want to check? "))

if number % 2 == 0:
    print("This is an even number.")
else:
    print("This is an odd number.")