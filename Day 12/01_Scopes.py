######## SCOPES #######
# It is like apple tree inside our home so only we can access but if apple tree is at
# roadside then everyone can access
enemies = 1

def increase_enemies():
    enemies = 2
    print(f"enemies inside function : {enemies}")

increase_enemies()
print(f"enemies outside function : {enemies}")

####### LOCAL SCOPES #########

# def drink_potion():
#     potion_strength = 2
#     print(potion_strength)

# drink_potion()
# print(potion_strength) 
# Although we have defined potion_strength inside function we get error that it is 
# not defined

####### GLOBAL SCOPES  #####
player_health = 10

def game():
    def drink_potion():
        potion_strength = 2
        print(player_health) # As global variable we can access from anywhere

# drink_potion() # can't access from here as it inside game()
    drink_potion()
print(player_health)



