# Write a program that calculates the average student height from a list of heights.
# e.g. student_heights = [180, 124, 165, 173, 189, 169, 146]

# The average height can be calculated by adding all the heights together and dividing by the total number of heights.
# e.g. 180 + 124 + 165 + 173 + 189 + 169 + 146 = 1146
# There are a total of 7 heights in student_heights, so 1146 ÷ 7 = 163.71428571428572
# Average height rounded to the nearest whole number = 164

# Important You should not use the sum() or len() functions in your answer. You should try to replicate their functionality using for loops.

total_height = 0 # Initialize the height sum to 0.
total_students = 0 # Initialize the student count to 0.

student_heights = input("Input a list of student heights ").split() # Example input: 156 178 165 171 187
for n in range(0, len(student_heights)): # Create a for loop with a range from 0 to the total length of the list.
  student_heights[n] = int(student_heights[n]) # Convert the inputted heights from string to integer.
  total_height += student_heights[n] # Keep track and increment the height sum each time we iterate.
  total_students += 1 # Keep track and increment the student count by 1 for each iteration.

average_height = total_height / total_students

print(f"The list of students is: {student_heights}.")
print(f"The total sum of students' heights is: {total_height}.")
print(f"The total number of students is: {total_students}.")
print(f"The average height of the students is: {round(average_height)}.")

  

  