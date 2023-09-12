# Instruction: https://app.codingrooms.com/w/8Ujw2Yy3xN4p

# Write a program that will mark a spot with an X.
# In the starting code, you will find a variable called map.
# This map contains a nested list. When map is printed this is what the nested list looks like:

# [['⬜️', '⬜️', '⬜️'],['⬜️', '⬜️', '⬜️'],['⬜️', '⬜️', '⬜️']]

# This is a bit hard to work with. So we've used this line of code print(f"{row1}\n{row2}\n{row3}" to format the 3 lists to be printed as a 3 by 3 square, each on a new line. 

# ['⬜️', '⬜️', '⬜️']
# ['⬜️', '⬜️', '⬜️']
# ['⬜️', '⬜️', '⬜️']

# Now it looks a bit more like the coordinates of a real map:
# Example: https://codingrooms-user-uploads-us-west-2.s3-us-west-2.amazonaws.com/dcf3f486-3ca7-40e2-8c2c-3e7ed90ea071/Co-ordinates_oggjzg+copy.png

# Your job is to write a program that allows you to mark a square on the map using a two-digit system. 
# The first digit in the input will specify the column (the position on the horizontal axis).
# The second digit in the input will specify the row number (the position on the vertical axis). 
# So an input of 23 should place an X at the position shown below:
# Example: https://codingrooms-user-uploads-us-west-2.s3-us-west-2.amazonaws.com/67152b41-0349-4387-81ad-896f9c069c48/Day+4+Treasure+Map+Updated.png

# First, your program must take the user input and convert it to a usable format.
# Next, you need to use that input to update your nested list with an "x". Remember that your nested list map actually looks like this: [['⬜️', '⬜️', '⬜️'],['⬜️', '⬜️', '⬜️'],['⬜️', '⬜️', '⬜️']].

# Define the initial map
row1 = ["⬜️", "️⬜️", "️⬜️"]
row2 = ["⬜️", "⬜️", "️⬜️"]
row3 = ["⬜️️", "⬜️️", "⬜️️"]
map = [row1, row2, row3]

# Display the initial map
print(f"{row1}\n{row2}\n{row3}")

# Start a loop that will continue until valid coordinates are entered
while True:
    # Get user input for coordinates
    position = input("Where do you want to put the treasure? ")

    # Check if the input has exactly two characters
    if len(position) == 2:
        # Convert the characters to integers and subtract 1 to adjust to Python indices
        row = int(position[0]) - 1
        column = int(position[1]) - 1

        # Check if the coordinates are within the valid map limits
        if 0 <= row < len(map[0]) and 0 <= column < len(map):
            # Display the coordinates and mark the location with "X"
            print(f"Row: {row + 1}. | Column: {column + 1}")
            map[column][row] = "X"
            break  # Exit the loop when valid coordinates are entered
        else:
            print("Coordinates out of range.")  # Error message if coordinates are out of range
    else:
        print("Please, type only two characters.")  # Error message if input doesn't have exactly two characters

# Display the updated map
print(f"{row1}\n{row2}\n{row3}")


