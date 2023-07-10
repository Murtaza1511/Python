# Dictionary is key-value pair
programming_dictionary = {"bug" : "an error in programming which prevents us from getting expected O/P",
                          "function":"a piece of code that can be easily called over and over again"}

# Retrieving items from dictionary
print(programming_dictionary["bug"])

# We get KeyError if we try to access a key which is NOT present in dictionary
# print(programming_dictionary["jhdfbjn"])

# Adding new items to the dictionary
programming_dictionary["loop"] = "action which executed over and over again"

# Creating a empty dictionary
empty_dictionary = {}

# Wiping out an existing dictionary
# programming_dictionary = {}

# Editing an item in a dictionary
# If the key is already present its value will be changed , else a new key-value pair will be inserted
programming_dictionary["bug"] = "a moth in computer"
print(programming_dictionary)

# Looping through a dictionary 
# NOTE:- We will get key when we will iterate through a dictionary
for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])