# You are given two sorted arrays that both only contain integers. Your task is to find a way to merge them into a single one, sorted in asc order. Complete the function mergeArrays(arr1, arr2), where arr1 and arr2 are the original sorted arrays.

# You don't need to worry about validation, since arr1 and arr2 must be arrays with 0 or more Integers. If both arr1 and arr2 are empty, then just return an empty array.

# Note: arr1 and arr2 may be sorted in different orders. Also arr1 and arr2 may have same integers. Remove duplicated in the returned result.

# Examples (input -> output)
# * [1, 2, 3, 4, 5], [6, 7, 8, 9, 10] -> [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# * [1, 3, 5, 7, 9], [10, 8, 6, 4, 2] -> [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# * [1, 3, 5, 7, 9, 11, 12], [1, 2, 3, 4, 5, 10, 12] -> [1, 2, 3, 4, 5, 7, 9, 10, 11, 12]

# My answer:

def merge_arrays(arr1, arr2):
    arr3 = []
    arr3 += arr1 + arr2
    n = -1
    sort = sorted(arr3)  
    for i in sort:
        n += 1  
        index = sort.index(i, n)
        if sort[index] == sort[index-1]:
            sort.remove(i)
    return sort

[-98, -96, -90, -86, -84, -81, -77, -76, -73, -72, -67, -66, -56, -55, -54, -53, -51, -47, -44, -42, -41, -39, -38, -37, -36, -31, -30, -22, -21, -20, -19, -17, -15, -12, -10, -8, -1, 0, 1, 2, 5, 9, 10, 17, 20, 21, 22, 23, 27, 28, 31, 32, 33, 34, 39, 41, 43, 50, 54, 55, 58, 59, 62, 64, 68, 71, 72, 74, 81, 82, 87, 91, 93, 94, 95, 97, 98]

print(merge_arrays([-96, -77, -73, -72, -67, -66, -55, -51, -51, -38, -37, -20, -19, -17, -12, -12, -8, -1, 0, 5, 9, 17, 17, 20, 28, 32, 33, 34, 41, 43, 50, 54, 55, 58, 59, 71, 91, 94, 95, 97], [98, 97, 93, 87, 87, 82, 81, 74, 72, 68, 64, 62, 50, 39, 32, 31, 27, 23, 22, 21, 21, 10, 10, 2, 1, -10, -15, -20, -21, -22, -30, -30, -31, -36, -39, -39, -41, -42, -44, -47, -53, -53, -54, -55, -55, -56, -67, -76, -81, -84, -86, -90, -98]))