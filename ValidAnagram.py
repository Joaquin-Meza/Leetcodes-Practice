"""
Given two strings s and t, return true if the 2 strings are anagrams of each other, otherwise, return false.

An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.
"""

def isAnagram_sorting(s,t):
    """
    Validate if the input strings are anagrams of each other using sorting
    :param s:
    :param t:
    :return:
    """
    # Edge case
    if len(s) != len(t):
        return False

    s_sorted = sorted(s)
    t_sorted = sorted(t)
    if s_sorted == t_sorted:
        return True
    else:
        return False


def isAnagram(s, t):
    """
    Validate if the input strings are anagrams of each other using Hash table
    :param s:
    :param t:
    :return:
    """
    # Edge case
    if len(s) != len(t):
        return False

    countS, countT = {}, {}

    for i in range(len(s)):
        countS[s[i]] = 1 + countS.get(s[i], 0)
        countT[t[i]] = 1 + countT.get(t[i], 0)
    return countS == countT



# Example 1
s = "racecar"
t = "carrace"

print(isAnagram(s, t))

# Example 2
s = "jar"
t = "jam"

print(isAnagram(s, t))


