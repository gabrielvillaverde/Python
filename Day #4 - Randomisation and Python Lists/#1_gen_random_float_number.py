# 1: Generate a random floating number using the random.random() method in Python [between 0 and 1, not including 1].

import random
float_random_number = random.random()
print(f"First exercise: {float_random_number}.")

# 2: Generate a random floating number using the random.random() method in Python [between 0 and 5, not including 5].

# Adding method:
int_random_number = random.randint(0,4)
second_float_random_number = random.random()
new_random_number = second_float_random_number + int_random_number
print(f"Second exercise, first solution: {new_random_number}.")

# Multiplying method:
mult_float_random_number = float_random_number * 5
print(f"Second exercise, second solution: {mult_float_random_number}.")
