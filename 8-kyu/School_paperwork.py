# Your classmates asked you to copy some paperwork for them. You know that there are 'n' classmates and the paperwork has 'm' pages.

# Your task is to calculate how many blank pages do you need. If n < 0 or m < 0 return 0.

# Example:
# n= 5, m=5: 25
# n=-5, m=5:  0

# My answer:
def paperwork(n, m):
    if n<1 or m<1: 
        blank = 0
    else:
        blank = n * m
    return blank

print(paperwork(1, 4))