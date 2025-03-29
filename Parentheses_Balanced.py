"""
Stacks - Parenthesis Balanced

Check to see if a string of a parentheses is balanced or not.

"Balanced" -> For every open parenthesis, there is a matching closing parenthesis in the correct order.
For example, the string "((()))" has three pairs of balanced parentheses, so it is a balanced string.

Your program should take a string of parentheses as input and return True if it is balanced,
or False if it is not. In order to solve this problem, use a Stack.
"""

def is_balanced_parentheses(string):
    # Edge case
    if len(string) == 0 or len(string)%2 !=0:
        return False

    stack = []      # Create stack to store the open parentheses

    for parenthesis in string:
        if parenthesis == '(':
            stack.append(parenthesis)
        elif parenthesis == ')':
            if len(stack) == 0 or stack.pop() != '(':
                return False

    return len(stack) == 0

string = "()"
print(is_balanced_parentheses(string))