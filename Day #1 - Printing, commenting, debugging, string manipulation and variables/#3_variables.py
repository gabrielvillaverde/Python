# Write a program that switches the values stored in the variables a and b.

# Warning. Do not change the code on lines 6-9 and 20-25. 
# Your program should work for different inputs. e.g. any value of a and b.

a = input("a: ")
b = input("b: ")

new_a_value = b
new_b_value = a

a = new_a_value
b = new_b_value

print("a: " + a)
print("b: " + b)

num_hours = "5"
print("There are " + num_hours + " hours until midnight")