"""
Given an array of strings strs, group all anagrams together into sublists. You may return the output in any order.

An anagram is a string that contains the exact same characters as another string, but the order of the characters can
be different.
"""
from collections import defaultdict

def groupAnagrams_sorted(strs):
    # Edge case:
    if len(strs) == 0:
        return []

    hashtable = {}
    for element in strs:
        aux = ''.join(sorted(element))
        if aux not in hashtable:
            hashtable[aux] = [element]
        else:
            hashtable[aux].append(element)
    return list(hashtable.values())

def groupAnagrams(strs):
    # Group anagrams using hashmaps only
    # Assuming that all elements are lowercase and alphabetic, therefore a-z, 26 possible characters

    # Step 1 - Define the Hashmap were we are going to store all the strings as values, and the keys are the frequency
    # of characters in each string
    data = defaultdict(list)       # Hashmap to map the counted elements

    # Step 2 - Go through each string in the list
    for string in strs:     # For each string in the list of strings

        # Step 3 - Create a counter for each alphabetic character
        count = [0]*26  # Counter for each possible character [1,26]

        for char in string:
            # Map the character ASCII value and store it
            count[ord(char) - ord('a')] += 1    # Store the ASCII value as the key, and the frequency of the character as the value

        # Step 4 - Add the string to the hashmap according to its key
        data[tuple(count)].append(string)

    return list(data.values())




strs = ["act","pots","tops","cat","stop","hat"]
print(groupAnagrams(strs))
