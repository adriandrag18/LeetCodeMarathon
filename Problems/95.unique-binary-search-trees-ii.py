# title: Unique Binary Search Trees II
# timestamp: 2025-06-29 22:27:57
# problemUrl: https://leetcode.com/problems/unique-binary-search-trees-ii/
# memory: 23.5 MB
# runtime: 234 ms

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int, offset=1) -> List[Optional[TreeNode]]:
        if n == 0:
            return [None]
        
        if n == 1:
            return [TreeNode(offset)]
        
        res = []
        for i in range(n):
            root = TreeNode(i + offset)
            lefts = self.generateTrees(i, offset)
            tmp = [deepcopy(root) for _ in range(len(lefts))]
            for r, left in zip(tmp, lefts):
                r.left = left
            rights = self.generateTrees(n - 1 - i, offset + i + 1)
            for right in rights:
                t = deepcopy(tmp)
                for r in t:
                    r.right = deepcopy(right)
                res.extend(t)
        
        return res

            