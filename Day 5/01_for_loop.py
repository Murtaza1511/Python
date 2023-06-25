# We can go to haveibeenpwned.com to see whether our account is compromised 
# Loops are used to iterate a set of statements over and over again
# For example when we do mischief we need to write a statement 
# 100 times
fruits = ['Apple', 'Pineapple', 'Peach']
for fruit in fruits:
    print(fruit)
    print(fruit+" Pie")
    # Indented so that statement is inside for loop
print(fruits)

# for with range()
print("Multiples of 3")
for i in range(3,100,3):
    print(i)
sum = 0
for i in range(1,101):
    sum += i

print(f'The sum from 1 to 100 is {sum}')
