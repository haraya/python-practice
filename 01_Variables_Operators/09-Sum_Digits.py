"""
Define an integer variable number with a three-digit value (e.g., 123).
Calculate and print the sum of its digits (1 + 2 + 3).
"""

#Variables
number = 135
sum_digits = 0


#Calculate
while number > 0:
    digit = number % 10
    print(number)
    sum_digits += digit
    number //=10
    print(number)


#Printing
print(sum_digits)

