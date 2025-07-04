# title: Path Sum III
# timestamp: 2024-12-30 14:51:39
# problemUrl: https://leetcode.com/problems/path-sum-iii/
# memory: 28.1 MB
# runtime: 171 ms

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        self.res = 0
        def dfs(root, li):
            if not root: 
                return
            # liL, liR = li[:], li[:]
            li.append(0)
            for i in range(len(li)):
                li[i] += root.val
                if li[i] == targetSum:
                    self.res +=1
            
            dfs(root.left, li[:])
            dfs(root.right, li)

        dfs(root, [])
        return self.res