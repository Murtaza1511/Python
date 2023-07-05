def greet():
    print('Hello')
    print('How are you')
    print('Hope you are fine')
greet()

# functions with inputs
def greet_with_name(name): # name is parameter
    print('Hello',name)
    print('How are you')
greet_with_name('Murtaza') # 'Murtaza' is argument

# functions with more than one input i.e. positional arguments
def greet_with(name,location):
    print('Hello',name)
    print('How is the weather at',location)

greet_with('Mur','Rajkot')

# functions with keyword arguments
def greet_student(name,rollno,grade):
    print('Hello',name)
    print('Your rollno is',rollno)
    print('Your grade is',grade)
greet_student(rollno=32,name='Murtaza',grade='A')

    
