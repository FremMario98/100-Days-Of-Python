# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


# Write your code below this row 👇
student_count = 0
students_height_sum = 0
for height in student_heights:
    students_height_sum += height
    student_count += 1

average_height = round(students_height_sum / student_count)
print(f"Average height: {average_height}")

# Or short answer
# average_height = round(sum(student_heights)/len(student_heights))
# print(f"Average height: {average_height}")
