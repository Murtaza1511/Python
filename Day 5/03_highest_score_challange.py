student_scores = input('Input a list of student heights').split()
for n in range(0,len(student_scores)):
    student_scores[n] = int(student_scores[n])
print(student_scores)

highest = student_scores[0]
for score in student_scores:
    if highest < score:
        highest = score
print(f'The highest score is : {highest}')