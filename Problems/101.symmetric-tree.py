# title: Symmetric Tree
# timestamp: 2024-12-31 15:31:23
# problemUrl: https://leetcode.com/problems/symmetric-tree/
# memory: 17.8 MB
# runtime: 0 ms

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        lvl, newLvl, nums = [root], [], []
        while lvl:
            for node in lvl:
                if node.left:
                    newLvl.append(node.left)
                    nums.append(node.left.val)
                else:
                    nums.append(-100000)

                if node.right:
                    newLvl.append(node.right)
                    nums.append(node.right.val)
                else:
                    nums.append(-100000)
                
            if nums != nums[::-1]:
                return False

            lvl, newLvl, nums = newLvl, [], []
        
        return True