# Our Name
# His/ Her Name
# T  L
# R  O
# U  V
# E  E
# x  y then you're xy % compatible for each other
print('Welcome to the Love Calculator')
name1 = input("What is your name \n")
name2 = input("What is their name \n")
first = 0
name1 = name1.lower()
name2 = name2.lower()
t = name1.count('t') + name2.count('t')
r = name1.count('r') + name2.count('r')
u = name1.count('u') + name2.count('u')
e = name1.count('e') + name2.count('e')
first = t+r+u+e

second = 0
l = name1.count('l') + name2.count('l')
o = name1.count('o') + name2.count('o')
v = name1.count('v') + name2.count('v')
e = name1.count('e') + name2.count('e')
second = l+o+v+e
percent = int(str(first)+str(second))
# percent = int(percent)

if percent < 10 or percent > 90:
    print(f"Your score is {percent}, you go together like coke and mentos")
elif percent >= 40 and percent < 50:
    print(f"Your score is {percent},you are alright together")
else:
    print(f"Your score is {percent}")