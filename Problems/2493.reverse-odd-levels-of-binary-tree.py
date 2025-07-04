# title: Reverse Odd Levels of Binary Tree
# timestamp: 2024-12-21 01:02:21
# problemUrl: https://leetcode.com/problems/reverse-odd-levels-of-binary-tree/
# memory: 22.8 MB
# runtime: 7 ms

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root
        
        lvl, newLvl = [root], []
        reverse = True
        while lvl:
            for node in lvl:
                if not node.left:
                    break
                newLvl.append(node.left)
                newLvl.append(node.right)
            if reverse:
                # print(*zip([n.val for n in newLvl], [n.val for n in newLvl[::-1]]))
                for node, val in zip(newLvl, [n.val for n in newLvl[::-1]]):
                    node.val = val
            # print([n.val for n in lvl], [n.val for n in newLvl], reverse)
            lvl, newLvl = newLvl, []
            reverse = not reverse
        
        return root
