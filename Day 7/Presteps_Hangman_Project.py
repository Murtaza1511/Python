import random
# We need to first draw flowchart in order to make any project
# Step 1
# Create a random word 
# word_list = ['camel','horse','elephant']
# word_chosen = random.choice(word_list)
# print(word_chosen)
# guess = input('Guess a letter: ').lower()
# for letter in word_chosen:
#     if guess == letter:
#         print('Right')
#     else:
#         print('Wrong')


# Step 2
# Now will create a list of same length as of the word_chosen and 
# initialize it with underscore and replace the letter with _ if 
# the guess is correct
# chosen_list = []
# for letter in word_chosen:
#     chosen_list += '_' # We can also use append() here
# print(chosen_list)

# for i in range(len(word_chosen)):
#     if word_chosen[i] == guess:
#         chosen_list[i] = guess
# print(chosen_list)


# Step 3
# We will let user enter the letter until all letter in the list are  
# letter other than underscore

# My Way
# while chosen_list.count('_') != 0:
#     guess = input('Guess a letter: ').lower()
#     for i in range(len(word_chosen)):
#         if word_chosen[i] == guess:
#             chosen_list[i] = guess
#             print(chosen_list)

# Another Way
# end_of_game = False
# while not end_of_game:
#     guess = input('Guess a letter: ').lower()
#     for i in range(len(word_chosen)):
#         if word_chosen[i] == guess:
#             chosen_list[i] = guess
#             print(chosen_list)
#         if '_' not in chosen_list:
#             end_of_game = True



#Step 4


stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']


#TODO-1: - Create a variable called 'lives' to keep track of the number of lives left. 
#Set 'lives' to equal 6.

#TODO-2: - If guess is not a letter in the chosen_word,
#Then reduce 'lives' by 1. 
#If lives goes down to 0 then the game should stop and it should print "You lose."

#TODO-3: - print the ASCII art from 'stages' that corresponds to the current number of 'lives' the user has remaining.

lives = 6

word_list = ['camel','horse','elephant']
word_chosen = random.choice(word_list)
print(word_chosen)

chosen_list = []
for letter in word_chosen:
    chosen_list += '_' # We can also use append() here


end_of_game = False
while not end_of_game:
    guess = input('Guess a letter: ').lower()
    for i in range(len(word_chosen)):
        if word_chosen[i] == guess:
            chosen_list[i] = guess
            
            
            
    if guess not in word_chosen:
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose! ")

    print(f"{' '.join(chosen_list)}")
            
    if '_' not in chosen_list:
                end_of_game = True
                print('You win')

    print(stages[lives])