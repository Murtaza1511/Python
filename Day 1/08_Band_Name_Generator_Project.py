print('Welcome to Band Name Generator')
city_name = input("""What's the name of the city you grew up in?\n""")
pet_name = input('''What's your pet name?\n''')
print('Your brand name could be '+city_name + ' '+pet_name)
liked = input('Did you liked the name? or want another name: Yes or No\n')
if(liked == 'No'):
    print('Your brand name could be '+pet_name + ' '+city_name)
