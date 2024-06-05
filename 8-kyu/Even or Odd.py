# Create a function that takes an integer as an argument and returns "Even" for even numbers or "Odd" for odd numbers.

# My answer:
def even_or_odd(number):
    if number %2 == 0:
        return "Even"
    else:
        return "Odd"

print(even_or_odd(1))
