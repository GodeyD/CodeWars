# Complete the square sum function so that it squares each number passed into it and then sums the results together.

# For example, for [1, 2, 2] it should return 9 because 1**2 + 2**2 + 2**2 =9 1**2 +2**2 +2**2 =9.

# My answer:
def square_sum(numbers):
    sum = 0
    for n in numbers:  
        sum += n**2
    return sum

print(square_sum([1, 2, 2]))