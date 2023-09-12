print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

first_option = input("Which direction do you want to go, left or right?\n").lower()

# LEFT option - KEEP GOING.
if first_option == "l" or first_option == "left":
    print(f"You chose the left corridor, you venture into a sinister one filled with darkness and a lot of water. You can continue the journey.")
    
    second_option = input("What would you do? Swim or wait?\n").lower()
    
    # WAIT option - KEEP GOING.
    if second_option == "w" or second_option == "wait":
        print("It seems like nothing is happening. After a couple of minutes, you decide to continue the journey.")
        
        third_option = input("You are now facing three doors: red, yellow and blue. Which one do you choose?\n").lower()
        
        # YELLOW door option - WIN THE GAME.
        if third_option == "y" or third_option == "yellow":
            print("You've reached the treasure room! You've obtained a loot of $10,000. You've won the game!")
        
        # RED door option - GAME OVER.
        elif third_option == "r" or third_option == "red":
            print("You've been burned by fire: GAME OVER.")
        
        # BLUE door option - GAME OVER.
        elif third_option == "b" or third_option == "blue":
            print("You've been eaten by beasts: GAME OVER.")
        else:
            print("That's not even an option. GAME OVER.")       
                         
    # SWIM or anything else option - GAME OVER.
    else:
        print("You've been attacked by trout: GAME OVER.")
        
# RIGHT or anything else option - GAME OVER
else:
    print("You fall into a hole: GAME OVER.")
    