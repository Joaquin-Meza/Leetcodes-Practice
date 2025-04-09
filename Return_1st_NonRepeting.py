"""
Given a string, return the first non-repeating character

"""

def solution(string):
    table = {}

    # 1st go through all the elements in the string and count the number of apperances
    for c in string:
        table[c] = table.get(c, 0)+1

    # 2nd go through the order of the elements in the string and check for the firs non-repeating element
    for key in string:
        if table[key] == 1:
            return key

    # In case that the string is empty or there are non-repeating elements
    return "_"

example1 = "abcadc"
example2 = "aa"
example3 = "bacc"
print(solution(example3))