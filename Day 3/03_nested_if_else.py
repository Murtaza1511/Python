# Ticket Counter
print('Welcome to the Rollercoster')
height = int(input('Enter your height in cms : '))
if height >= 120:
    print("You can ride in the rollercoster , you are perfect!!")
    age = int(input('Enter your age : '))
    if age < 12:
        print('You will pay $5 for the ticket')
    elif age <= 18:
        print("You will pay $7 for ticket")
    else:
        print('You will pay $12 for the ticket')
else:
    print("Your height is small you can't ride ")