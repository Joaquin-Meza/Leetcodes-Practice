"""
Given an integer array nums, return true if any value appears more than once in the array, otherwise return False
"""

def containDuplicates(nums):
    hashset = set()
    for num in nums:
        if num in hashset:
            return True
        hashset.add(num)
    return False


# Example
nums = [1, 2, 3, 3]
print(containDuplicates(nums))

nums = [1, 2, 3, 4]
print(containDuplicates(nums))

