# title: Populating Next Right Pointers in Each Node II
# timestamp: 2025-06-20 00:08:00
# problemUrl: https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/
# memory: 18.9 MB
# runtime: 42 ms

"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root
            
        lvl, new = [root], []
        while lvl:
            for node in lvl:
                if node.left:
                    new.append(node.left)
                if node.right:
                    new.append(node.right)

            for i in range(len(lvl) - 1):
                lvl[i].next = lvl[i+1]
            
            lvl, new = new, []
        
        return root