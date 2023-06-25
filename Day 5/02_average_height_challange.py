student_heights = input('Input a list of student heights').split()
for n in range(0,len(student_heights)):
    student_heights[n] = int(student_heights[n])
print(student_heights)

sum = 0
for student_height in student_heights:
    sum += student_height

avg = sum // len(student_heights)
print(f"The average height of students is {avg} ")



