"""
The function takes a single parameter string, which is the string you want to reverse.
Return a new string with the letters in reverse order.
"""

def reverse_string(string):
    new_string = []
    for element in range(len(string)-1, -1, -1):
        new_string.append(string[element])
    return ''.join(new_string)

string = "hola"
print(reverse_string(string))