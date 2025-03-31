"""
Binary Search Tree
Convert Sorted List to Balanced BST

Objective:
The task is to develop a method that takes a sorted list of
integers as input and constructs a height-balanced BST.

This involves creating a BST where the depth of the two  subtrees of any
node does not differ by more than once.

Achieving a height-balanced tree is crucial for optimizing the efficiency
of tree operations, ensuring that the BST remains efficient for search, insertion,
and deletion across all levels of the tree
"""


# Create BST class
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def is_balanced(self, node=None):
        def check_balance(node):
            if node is None:
                return True, -1
            left_balanced, left_height = check_balance(node.left)
            if not left_balanced:
                return False, 0
            right_balanced, right_height = check_balance(node.right)
            if not right_balanced:
                return False, 0
            balanced = abs(left_height-right_height) <= 1
            height = 1 + max(left_height, right_height)
            return balanced, height

        balanced, _ = check_balance(self.root if node is None else node)
        return balanced

    def inorder_traversal(self,node=None):
        if node is None:
            node = self.root
        result = []
        self._inorder_helper(node, result)
        return result

    def _inorder_helper(self,node, result):
        if node:
            self._inorder_helper(node.left, result)
            result.append(node.value)
            self._inorder_helper(node.right, result)

    def sorted_list_to_bst(self, nums):
        self.root = self._sorted_list_to_bst(nums,0,len(nums)-1)

    def _sorted_list_to_bst(self, nums, left, right):
        """
        Description: Private method to convert sorted list to a BST. The method used the middle element of the list
        as the root to ensure balanced height.

        - The function is recursively called to construct the left and right subtrees.
        - A new Node is created at each recursive call with the mid element of the current list segment as its value,
        ensuring the BST property is maintained.
        Parameters:
        :param nums: Sorted list of integers.
        :param left: Starting index of the list segment.
        :param right: Ending index of the list segment.
        :return: The root node of the BST created from the specified list segment
        """
        # Base condition: if left index is greater than right index, then we have considered all elements in this segment
        if left > right:
            return None
        # Find he middle index of the current segment of the list
        mid = (left+right)//2
        # Create a new Node instance using the value at the middle index
        current = Node(nums[mid])
        # Recursively build the left and right subtrees
        # The function calls itself with the current segment adjusted to the left or right half excluding the middle element
        current.left = self._sorted_list_to_bst(nums, left, mid-1)
        current.right = self._sorted_list_to_bst(nums, mid+1, right)

        return current

