# title: Recover a Tree From Preorder Traversal
# timestamp: 2025-02-22 15:09:11
# problemUrl: https://leetcode.com/problems/recover-a-tree-from-preorder-traversal/
# memory: 19.1 MB
# runtime: 23 ms

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        nodes = []
        depth, num = 0, 0
        for c in traversal:
            if c == '-':
                if num != 0:
                    nodes.append((num, depth))
                    depth, num = 0, 0
                depth += 1
                continue
            
            if c.isdigit():
                num = 10 * num + int(c)
                continue
        if num != 0:
            nodes.append((num, depth))
        
        print(nodes)
        root = TreeNode(nodes[0][0])
        index = 1
        
        def helper(root, depth):
            nonlocal index
            if index == len(nodes) or nodes[index][1] < depth:
                return

            root.left = TreeNode(nodes[index][0])
            index += 1
            helper(root.left, depth + 1)    
            
            if index == len(nodes) or nodes[index][1] < depth:
                return

            root.right = TreeNode(nodes[index][0])
            index += 1
            helper(root.right, depth + 1)

        helper(root, 1)
        return root