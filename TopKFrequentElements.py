"""
Given an integer array nums and an integer k, return the k most frequent elements
within the array.

You may return the output in any order
"""

def topKFrequent(nums, k):
    if len(nums) == 0:
        return []

    # 1. Crate a hashmap with every element and its frequency
    counter = {}
    for num in nums:
        counter[num] = 1 + counter.get(num, 0)

    # 2. Sorted it
    aux_array = []                          # Auxiliar array to store the num and its frequency, and then to be sorted
    for num, freq in counter.items():       # Create an array with the values of the hashmap [freq, num]
        aux_array.append([freq, num])
    aux_array.sort()                        # Sort the array in the order of greater frequency

    # Return the k top frequent elements
    res = []
    while len(res)<k:
        res.append(aux_array.pop()[1])      #  Pop the elements from the sorted array
    return res


nums = [1, 2, 2, 3, 3, 3]
k = 2
print(topKFrequent(nums, k))
