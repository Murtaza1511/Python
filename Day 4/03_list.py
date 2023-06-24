# Application: to do list
# For example we want to store states of america and ordering 
# is important as to when it joined union , so when ordering is needed
# then we use list

fruits = ['mango', 'apple', 'grapes']
states_of_america = ['Delaware' , 'Pennsylvania']
print(states_of_america[0])
print(states_of_america[-1])
print(states_of_america)

states_of_america.append('New Jersey')
states_of_america.extend(['Georgia' , 'Connecticut'])
print(states_of_america)
# If we try to access any index out of the range of elements present
# then it will gives us IndexError

# List of lists
vege = ['brinjal', 'carrot']
food = [vege,fruits]
print(food)