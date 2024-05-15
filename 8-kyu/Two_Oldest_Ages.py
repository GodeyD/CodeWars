# The two oldest ages function/method needs to be completed. It should take an array of numbers as its argument and return the two highest numbers within the array. The returned value should be an array in the format [second oldest age,  oldest age].

# The order of the numbers passed in could be any order. The array will always include at least 2 items. If there are two or more oldest age, then return both of them in array format.

# For example (Input --> Output):

# [1, 2, 10, 8] --> [8, 10]
# [1, 5, 87, 45, 8, 8] --> [45, 87]
# [1, 3, 10, 0]) --> [3, 10]

# My answer:
def two_oldest_ages(ages):
    age1 = 0
    age2 = 0
    index = 0
    for i, age in enumerate(ages, start=0):
        if age > age1:
            index = i
            age1 = age            
            print(index, age1)
    for age in ages:
        if age == age1:
            del ages[index]
            print(ages)
    for age in ages:
        if age > age2:
            age2 = age 
    return [age2, age1]

print(two_oldest_ages([53, 9, 42, 73, 88, 52, 48, 68, 97, 92, 96, 56, 84, 7, 4, 98, 2, 76, 63, 90, 24, 98, 9, 30, 45, 6, 34, 3, 82]))