# Python Pizza. Building an automatic pizza order program.
# Based on a user's order, work out their final bill:

#Small Pizza: $15
#Medium Pizza: $20
#Large Pizza: $25

#Pepperoni for Small Pizza: +$2
#Pepperoni for Medium or Large Pizza: +$3
#Extra cheese for any size pizza: + $1

# WARNING: This solution does not follow good conditional practices as it repeats a significant amount of code.

print("Welcome to Python pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")

if size == "S":
    bill = 15
    print(f"You are ordering a small pizza. Base bill: ${bill}")
    if add_pepperoni == "Y":
        bill += 2
        print(f"You are adding pepperoni ($2) for a small pizza. Now the bill is: ${bill}")
    else:
        print(f"You are not adding pepperoni for a small pizza. The bill is still: ${bill}")
        
if size == "M":
    bill = 20
    print(f"You are ordering a medium pizza. Base bill: ${bill}")
    if add_pepperoni == "Y":
        bill += 3
        print(f"You are adding pepperoni ($3) for a medium pizza. Now the bill is: ${bill}")
    else:
        print(f"You are not adding pepperoni for a medium pizza. The bill is still: ${bill}")
        
if size == "L":
    bill = 25
    print(f"You are ordering a large pizza. Base bill: ${bill}")
    if add_pepperoni == "Y":
        bill += 3
        print(f"You are adding pepperoni ($3) for a large pizza. Now the bill is: ${bill}")
    else:
        print(f"You are not adding pepperoni for a large pizza. The bill is still: ${bill}")
        
if extra_cheese == "Y":
    bill += 1
    print(f"You are adding extra cheese ($1) for your {size} size pizza. The bill is now: ${bill}")
else:
    print(f"You are not adding extra cheese for a {size} size pizza. The bill is still: ${bill}")

        

