# Create a tip calculator.

# The calculator should take into account the total bill, the percentage of tip you want to leave, and the number of people splitting the bill. 
# Through programming, you will calculate the tip amount, the total bill including the tip, and the amount each person should pay."
# e.g.: If the bill was $150.00, split between 5 people, with 12% tip. Each person should pay (150.00 / 5) * 1.12 = 33.6
# Format the result to 2 decimal places = 33.60

#Write your code below this line 👇

# FIRST SOLUTION:
print("Welcome to the tip calculator!")

bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10, 12 or 15? "))
people = int(input("How many people to split the bill? "))

tip_as_percent = tip / 100
print(f"Tip as percent: {tip_as_percent}")

total_tip_amount = bill * tip_as_percent
print(f"Total tip amount: {total_tip_amount}")

total_bill = bill + total_tip_amount
print(f"Total bill including tip: {total_bill}")

bill_per_person = total_bill / people
print(f"Each person should pay: ${bill_per_person:.2f}.") # It is necessary to use :.2f

# SECOND SOLUTION (More limited because the existence of only three options, 10, 12 or 15):
# print("Welcome to the tip calculator!")

# total_bill = float(input("What was the total bill? $"))
# tip = int(input("What percentage tip would you like to give? 10, 12 or 15? "))
# people = int(input("How many people to split the bill? "))

# if tip == 10:
#     bill_per_person = (total_bill / people) * 1.10
# elif tip == 12:
#     bill_per_person = (total_bill / people) * 1.12
# elif tip == 15:
#     bill_per_person = (total_bill / people) * 1.15

# print(f"Each person should pay: ${bill_per_person:.2f}") # It is necessary to use :.2f