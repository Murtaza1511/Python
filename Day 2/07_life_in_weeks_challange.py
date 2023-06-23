# We assume that any person will live for 90 years only
age = int(input("What is your current age: "))
years_remaining = 90-age
months = years_remaining * 12
weeks = years_remaining * 52
days = years_remaining* 365
message = f"You have {days} days , {weeks} weeks {months} months "
print(message)