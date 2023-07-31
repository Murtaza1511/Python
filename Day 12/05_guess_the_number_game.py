import random 
# We can get the ascii art from text to ascii art website
def user_choosing(n,num):
    count = n
    i=0
    while i < n:
        print(f"You have {count} attempts remaining to guess the number")
        user_num = int(input('Make a choice: '))
        if user_num < num:
            print('Too low.\nGuess again.')
        elif user_num == num:
            print('You guessed it right')
            break
        else:
            print('Too high.\nGuess again.')
        i+=1
        count-=1
        if(i == n):
            print('You have run out of guesses. You lose! ')


print('Welcome to the Number Guessing Game!')
print("I'm thinking of a number between 1 and 100")
num = random.randint(1,100)

user_level = input("Choose a difficulty. Type 'easy' or 'hard': ")
if(user_level == 'easy'):
    user_choosing(10,num)
else:
    user_choosing(5,num)