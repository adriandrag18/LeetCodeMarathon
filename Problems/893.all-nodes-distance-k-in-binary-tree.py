# title: All Nodes Distance K in Binary Tree
# timestamp: 2025-06-22 11:51:36
# problemUrl: https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/
# memory: 18.1 MB
# runtime: 38 ms

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        def findDist(node, val, curr):
            if not node:
                return curr
            
            if node.val == val:
                node.dist = 0
            else:
                node.dist = curr
            
            l = findDist(node.left, val, node.dist + 1)
            r = findDist(node.right, val, node.dist + 1)
            
            node.dist = min([node.dist, l, r])
            
            return node.dist + 1
        
        def updateDist(node, dist):
            if not node:
                return
            
            node.dist = min(node.dist, dist)
            
            nonlocal res, k
            if node.dist == k:
                res.append(node.val)
            
            updateDist(node.left, node.dist + 1)
            updateDist(node.right, node.dist + 1)
        
        res = []
        findDist(root, target.val, float('inf'))
        updateDist(root, float('inf'))

        return res