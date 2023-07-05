def prime_checker(n):
    is_Prime = True 
    if n <=1:
        is_Prime = False
    for i in range(2,n):
        if n % i == 0:
            is_Prime = False
    if is_Prime == True:
        print("It's a Prime Number")
    else:
        print("It's Not a Prime Number")

n = int(input("Check this number! "))
prime_checker(n)

    