"""
Given an array of integers nums and integer target, return the indices i and j such that nums[i] + nums[j] == target
and i != j

You may assume that every input has exactly one pair of indices i and j that satisfy the condition
"""

def twoSum_v1(nums, target):
    # Edge case , when the nums array is empty
    if len(nums) == 0:
        return []

    data = {}       # Define hashtable
    for index, value in enumerate(nums):        # Store all the values and index of the elements in the array
        data[value] = index

    for index, value in enumerate(nums):        # Pass through the array and compute the complement using each value
        complement = target-value
        if complement in data and data[complement] != index:    # If the complement is in the hashtable, return the indeces
            return [index, data[complement]]


def twoSum(nums,target):
    data = {}

    for index, value in enumerate(nums):
        complement = target-value
        if complement in data:
            return [data[complement], index]
        data[value] = index

nums = [3, 4, 5, 6]
target = 7
print(twoSum(nums, target))
