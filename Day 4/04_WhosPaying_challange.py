# Who's paying at restaurant
import random

test_seed = int(input("Create a seed number: "))
random.seed(test_seed)

# Split the string method
nameasCSV = input("Give everybody's names , separated by comma : ")
names = nameasCSV.split(', ')

ind = random.randint(0,len(names)-1)
pay_name = names[ind]
print(f"{pay_name} is going to buy meal today")