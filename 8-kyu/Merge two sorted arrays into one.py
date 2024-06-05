# You are given two sorted arrays that both only contain integers. Your task is to find a way to merge them into a single one, sorted in asc order. Complete the function mergeArrays(arr1, arr2), where arr1 and arr2 are the original sorted arrays.

# You don't need to worry about validation, since arr1 and arr2 must be arrays with 0 or more Integers. If both arr1 and arr2 are empty, then just return an empty array.

# Note: arr1 and arr2 may be sorted in different orders. Also arr1 and arr2 may have same integers. Remove duplicated in the returned result.

# Examples (input -> output)
# * [1, 2, 3, 4, 5], [6, 7, 8, 9, 10] -> [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# * [1, 3, 5, 7, 9], [10, 8, 6, 4, 2] -> [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# * [1, 3, 5, 7, 9, 11, 12], [1, 2, 3, 4, 5, 10, 12] -> [1, 2, 3, 4, 5, 7, 9, 10, 11, 12]

# My answer:

def merge_arrays(arr1, arr2):               
    return sorted(list(set(arr1 + arr2)))


print(merge_arrays([-55], [98, 97, 93, 87, 87, 82, 81, 74, 72, 68, 64, 62, 50, 39, 32, 31, 27, 23, 22, 21, 21, 10, 10, 2, 1, -10, -15, -20, -21, -22, -30, -30, -31, -36, -39, -39, -41, -42, -44, -47, -53, -53, -54, -55, -55, -56, -67, -76, -81, -84, -86, -90, -98]))