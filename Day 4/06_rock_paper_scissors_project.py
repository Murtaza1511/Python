import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

user_choice = int(input('What do you choose? Type 0 for Rock , 1 for Paper or 2 for Scissors\n'))
computer_choice = random.randint(0,2)
if computer_choice == 0 and user_choice == 1:
    print(f"{paper}\nComputer chose:\n{rock}\nYou won!")
elif computer_choice == 1 and user_choice == 0:
    print(f"{rock}\nComputer chose:\n{paper}\nYou lose!")
elif computer_choice == 2 and user_choice == 1:
    print(f"{paper}\nComputer chose:\n{scissors}\nYou lose!")
elif computer_choice == 1 and user_choice == 2:
    print(f"{scissors}\nComputer chose:\n{paper}\nYou won!")
elif computer_choice == 0 and user_choice == 2:
    print(f"{scissors}\nComputer chose:\n{rock}\nYou lose!")
elif computer_choice == 2 and user_choice == 0:
    print(f"{rock}\nComputer chose:\n{scissors}\nYou won!")
elif computer_choice == 0 and user_choice == 0:
    print(f"{rock}\nComputer chose:\n{rock}\nYou both have a tie!")
elif computer_choice == 1 and user_choice == 1:
    print(f"{paper}\nComputer chose:\n{paper}\nYou both have a tie!")
elif computer_choice == 2 and user_choice == 2:
    print(f"{scissors}\nComputer chose:\n{scissors}\nYou both have a tie!")