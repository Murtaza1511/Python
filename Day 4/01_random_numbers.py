import random
import my_module # we can also import our own modules

print(my_module.pi)
random_integer = random.randint(1,10) #both inclusive
print(random_integer)
random_float = random.random() # inclusive of 0 and exclusive of 1
print(random_float)

rand_float = 5 * random.random()
print(rand_float)

love_score = random.randint(1,100)
print(f"Your love score is {love_score}")