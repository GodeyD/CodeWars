# At the annual family gathering, the family likes to find the oldest living family member’s age and the youngest family member’s age and calculate the difference between them.

# You will be given an array of all the family members' ages, in any order. The ages will be given in whole numbers, so a baby of 5 months, will have an ascribed ‘age’ of 0. Return a new array (a tuple in Python) with [youngest age, oldest age, difference between the youngest and oldest age].

# My answer:
def difference_in_ages(ages):
    ages.sort()
    return (ages[0], ages[-1], ages[-1] - ages[0])

print(difference_in_ages([16, 22, 31, 44, 3, 38, 27, 41, 88]))