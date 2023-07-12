from click import clear
from art import logo
# Add
def add(n1,n2):
    return n1+n2

# Subtract
def subtract(n1,n2):
    return n1-n2

# Multiplication
def multiply(n1,n2):
    return n1*n2

# Divide
def divide(n1,n2):
    return n1/n2

# Modulo division
def modulo(n1,n2):
    return n1%n2

# Power
def power(n1,n2):
    return n1**n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
    "%": modulo,
    "^": power
    }

def calculator():
    clear()
    print(logo)
    num1 = float(input("What's the first number? "))


    for operation in operations:
        print(operation)

    End = False
    while not End:
        operation_symbol = (input("Pick an operation from the line above: "))
        num2 = float(input("What's the next number? "))

        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1,num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")
        user_choice = input(f'Type "y" to continue calculation with {answer}, or type "n" to start new calculation: ')
        if user_choice == 'n':
            End = True
            calculator()
        num1 = answer

calculator()
# return v/s print 
# return is very useful if we want to use our function's O/P in other function
# or somewhere else in our program  