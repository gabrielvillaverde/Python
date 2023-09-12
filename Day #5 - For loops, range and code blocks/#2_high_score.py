#  Write a program that calculates the highest score from a list of scores.
# e.g. student_scores = [78, 65, 89, 86, 55, 91, 64, 89]

# Important: you are not allowed to use the max or min functions. The output words must match the example. 
# i.e. the highest score in the class is: x

student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)

max_score = 0 # Initialize new_max_note with the first element of the list.

for note in student_scores:
    if note > max_score:
        max_score = note

print(f"The highest score in the class is: {max_score}")


