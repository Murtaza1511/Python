print("Welcome to the tip calculator.")
amount = float(input("What was the total bill? $"))
tip_percent = int(input("What percentage tip you want to give? 10 , 12 , 15?"))
people = int(input("How many people to split the bill? "))
contri = amount / people
contri_with_tip = ((tip_percent/100)*contri) + contri
print(f"Each person should pay: ${round(contri_with_tip,2)}")

