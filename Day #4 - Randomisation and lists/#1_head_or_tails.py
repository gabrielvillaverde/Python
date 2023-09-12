# Write a virtual coin toss program. It will randomly tell the user "Heads" or "Tails".
# Important, the first letter should be capitalised and spelt exactly like in the example e.g. Heads, not heads.
# You should generate a random number, either 0 or 1. Then use that number to print out Heads or Tails.
# e.g. 1 means Heads, 0 means Tails

import random

random_number = random.randint(0,1)

if random_number == 1:
    print("Heads")
else:
    print("Tails")