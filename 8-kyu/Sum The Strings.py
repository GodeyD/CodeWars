# Create a function that takes 2 integers in form of a string as an input, and outputs the sum (also as a string):

# Example: (Input1, Input2 -->Output)

# "4",  "5" --> "9"
# "34", "5" --> "39"
# "", "" --> "0"
# "2", "" --> "2"
# "-5", "3" --> "-2"
# Notes:

# If either input is an empty string, consider it as zero.

# Inputs and the expected output will never exceed the signed 32-bit integer limit (2^31 - 1)

# My answer:
a = input('Enter a number: ')
b = input('number: ')

def sum_str(a, b):
    sum = 0
    if int(a) == 0:
        sum += int(a)
    else:
        sum += 0
    if int(b) == 0:
        sum += int(b)
    else:
        sum += 0   
    return sum

print(sum_str(a, b))