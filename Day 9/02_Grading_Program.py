"""
Scoring criteria
91-100 --> "Outstanding"
81-90 --> "Exceeds Expectation"
71-80 --> "Acceptable"
70 or lower --> "Fail"

"""



student_scores = {
    'Harry': 81,
    'Murtaza': 99,
    'Ron': 74,
    'Draco' : 62,
    'Neville': 78
}

# 🚨 Don't change the code above 👆

#TODO-1: Create an empty dictionary called student_grades.
student_grades = {}

#TODO-2: Write your code below to add the grades to student_grades.👇
for key in student_scores:
    # Instead of writing student_scores[key] everywhere we can declare score variable
    score = student_scores[key]
    if score >= 91:
        student_grades[key] = "Outstanding"
    elif score >= 81:
        student_grades[key] = "Exceeds Expectation"
    elif score >= 71:
        student_grades[key] = "Acceptable"
    else:
        student_grades[key] = "Fail"


    

# 🚨 Don't change the code below 👇
print(student_grades)

