# Water-level maintainer 
water_level = 50
if water_level > 80:
    print("Drain Water")
else:
    print("Continue")

# Ticket Counter for RollerCoster
print('Welcome to the Rollercoster')
height = int(input('Enter your height in cms : '))
if height == 120:
    print("You can ride in the rollercoster , you are perfect!!")
elif height > 120:
    print("You can ride ")
else:
    print("Your height is small you can't ride ")