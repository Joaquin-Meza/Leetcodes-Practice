"""
You are given two integer arrays num1 and num2, sorted in non-decreasing order, and two
integers m and n, representing the number of elements in nums1 and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, but instead be sorted inside the array nums1.
To accommodate this, num1 has a length of m+n, where the first m elements denote the elements
that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a lengths o n.
"""
#  0  1  2  3  4  5
# [1, 2, 3, 0, 0, 0]

def mergeSortedArray_bruteForce(nums1, m, nums2, n):
    # Brute force:
    nums1[m:] = nums2
    nums1.sort()



def mergeSortedArray(nums1, m, nums2, n):

    # Define auxiliar variables
    m_idx = m-1
    n_idx = n-1
    r_idx = m+n-1

    while n_idx >= 0:
        if m_idx >= 0 and nums1[m_idx] > nums2[n_idx]:
            nums1[r_idx] = nums1[m_idx]
            m_idx -= 1
        else:
            nums1[r_idx] = nums2[n_idx]
            n_idx -= 1
        r_idx -= 1


# Example
nums1 = [1, 2, 3, 0, 0, 0]
m = 3
nums2 = [2, 5, 6]
n = 3

print(nums1)
mergeSortedArray(nums1, m, nums2, n)
print(nums1)

print("Brute Force: ")
nums1 = [5, 7, 9, 0, 0, 0]
m = 3
nums2 = [1, 2, 3]
n = 3
print(nums1)
mergeSortedArray_bruteForce(nums1, m, nums2, n)
print(nums1)