# Add the two digits of a two digit number 
two_digit_number = int(input("Enter a two digit number"))
second = two_digit_number%10
first = two_digit_number //10
print(first+second)


#or
two_digit_number1 = input("Enter the number")
first_digit = int(two_digit_number1[0])
second_digit = int(two_digit_number1[1])
print(first_digit+second_digit)