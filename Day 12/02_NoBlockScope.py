# Python doesn't have block scope
game_level = 3
enemies = ['skeleton','alien','zombie']
if game_level < 5:
    new_enemy = enemies[0]
print(new_enemy)

def create_enemy():
    enemies = ['skeleton','alien','zombie']
    if game_level < 5:
        newest_enemy = enemies[0]
print(newest_enemy)
     