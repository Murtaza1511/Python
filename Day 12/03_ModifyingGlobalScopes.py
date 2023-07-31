# It is NOT suggested by many programmers as global variables enemies could be 
# somewhere in the program we don't know , so it is suggested to write a return statement
# for the same
enemies = 1

def increase_enemies():
    global enemies
    enemies += 1
    print(f"enemies inside function : {enemies}")

increase_enemies()
print(f"enemies outside function : {enemies}")
