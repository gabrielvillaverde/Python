# You are painting a wall. The instructions on the paint can says that 1 can of paint can cover 5 square meters of wall. 
# Given a random height and width of wall, calculate how many cans of paint you'll need to buy.

# Number of cans = (WALL HEIGHT * WALL WIDTH) ÷ COVERAGE PER CAN (in this case it will always be 5).
# e.g. Height = 2, Width = 4, Coverage = 5 | So the calculate is: (2 * 4) / 5 to determine the number of paint cans we need.
# But because you can't buy 1.6 of a can of paint, the result should be rounded up to 2 cans.

import math # Library to use math.ceil function to round up numbers.

def paint_calc(height, width, cover):
    paint_can_needed = (test_h * test_w) / coverage
    print(f"You'll need {math.ceil(paint_can_needed)} cans of paint.")

test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)

