# Complete the solution so that it reverses the string passed into it.

# 'world'  =>  'dlrow'
# 'word'   =>  'drow'

# My answer:
def solution(string):
    str = ""
    for w in string:
        str = w + str
    return str

print(solution('world'))