height = float(input("Enter your height in m : "))
weight = float(input("Enter your weight in kg : "))
bmi = round(weight / height ** 2,2)
if bmi < 18.5:
    print("You are Underweight")
elif bmi < 25:
    print("You are normal weight")
elif bmi < 30:
    print('You are overweight')
elif bmi < 35:
    print("You are obese")
else:
    print("You are clinically obese")