# title: Convert Sorted Array to Binary Search Tree
# timestamp: 2024-12-31 15:39:36
# problemUrl: https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/
# memory: 18.9 MB
# runtime: 4 ms

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None
        mid = len(nums) // 2
        return TreeNode(nums[mid], self.sortedArrayToBST(nums[:mid]), self.sortedArrayToBST(nums[mid+1:]))
        