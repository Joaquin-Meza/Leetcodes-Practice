"""
Design an algorithm to encode a list of strings to a single string. The encoded string
is then decoded back to the original list of strings.
"""

def encode(strs):
    # Proposed encode code: size of the string + "#" + string
    data = ""
    for string in strs:
        data = data + str(len(string))+'#'+string
    return data


strs = ["hello","there","General","kenovi"]
encoded_string = encode(strs)
print("Encoded string: ", encoded_string)


def decode(string):
    # Decode input string following the pattern: size of the string + "#" + string
    data = []
    outer_count = 0
    while outer_count < len(string):        # While we are inside the string limit size
        inner_count = outer_count
        while string[inner_count] != '#':       # Update the counter until we find the separator element "#"
            inner_count += 1
        length = int(string[outer_count:inner_count])   # Determine the size of the word
        data.append(string[inner_count + 1:inner_count + 1 + length])      # Append the string, ignoring the length int and the #
        outer_count = inner_count + 1 + length                         # Start the outer count after the first string
    return data


print("Decoded string: ", decode(encoded_string))
