import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Solution using if/else condition:

# game_images = [rock, paper, scissors]

print("Welcome to the Rock, Paper, and Scissors game.")

# while True:
#     while True:
#         try:
#             user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors.\n"))
#             if user_choice not in [0, 1, 2]:
#                 raise ValueError("Please enter a valid choice (0 for Rock, 1 for Paper, or 2 for Scissors).")
#             break
#         except ValueError as e:
#             print(f"Error: {e}. Please try again.")

#     print(f"You chose: \n{game_images[user_choice]}.")

#     pc_choice = random.randint(0, 2)
#     print(f"Computer chose: \n{game_images[pc_choice]}.")

#     if user_choice == pc_choice:
#         print("It's a draw")
#     elif (user_choice == 0 and pc_choice == 1) or (user_choice == 1 and pc_choice == 2) or (user_choice == 2 and pc_choice == 0):
#         print("You lose")
#     else:
#         print("You win!")

#     play_again = input("Do you want to play again? (yes/no): ").strip().lower()
#     if play_again != "yes":
#         break

# Solution using lists:

pics = [rock, paper, scissors]
 
your_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if your_choice < 0 or your_choice > 2 :
  print("Don\'t enter numbers out of scope!'")
  exit()
 
print(pics[your_choice])
 
comp_choice = random.randint(0,2)
print(f"Computer chose:\n{pics[comp_choice]}")
 
choice_matrix = [ ["It\'s a draw", "You lose", "You win"], # Rock option.
                ["You win", "It\'s a draw", "You lose"], # Paper option.
                ["You lose", "You win", "It\'s a draw"] ] # Scissors option.
print(choice_matrix[your_choice][comp_choice])

# If your_choice is 0 (rock) and comp_choice is 2 (scissors), the program will look up choice_matrix[0][2], resulting in "You win" because rock beats scissors.
# If your_choice is 1 (paper) and comp_choice is 0 (rock), the program will look up choice_matrix[1][0], resulting in "You win" because paper beats rock.
# If your_choice is 2 (scissors) and comp_choice is 1 (paper), the program will look up choice_matrix[2][1], resulting in "You win" because scissors beats paper.
