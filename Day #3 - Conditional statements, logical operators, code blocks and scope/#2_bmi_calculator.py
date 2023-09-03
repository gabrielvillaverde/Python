# In this coding exercise, you'll be creating a program that calculates the Body Mass Index (BMI) based on the user's height and weight inputs. 
# The BMI is then used to determine the user's weight category, whether it falls under "underweight," "normal weight," "slightly overweight," "obese," or "clinically obese."

height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))

import math

# Constants for BMI categories
UNDERWEIGHT = 18.5
NORMAL_WEIGHT = 25
SLIGHTLY_OVERWEIGHT = 30
OBESE = 35

# Calculate BMI and round it to one decimal place
bmi = math.ceil(weight / (height ** 2)) # math.ceil is used to round a floating-point number up to the nearest integer

# Determine BMI category and display message
if bmi < UNDERWEIGHT:
    print(f"Your BMI is {bmi}, you are underweight.")
elif bmi < NORMAL_WEIGHT:
    print(f"Your BMI is {bmi}, you have a normal weight.")
elif bmi < SLIGHTLY_OVERWEIGHT:
    print(f"Your BMI is {bmi}, you are slightly overweight.")
elif bmi < OBESE:
    print(f"Your BMI is {bmi}, you are obese.")
else:
    print(f"Your BMI is {bmi}, you are clinically obese.")
