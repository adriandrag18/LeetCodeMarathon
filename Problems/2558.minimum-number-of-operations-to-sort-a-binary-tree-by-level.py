# title: Minimum Number of Operations to Sort a Binary Tree by Level
# timestamp: 2024-12-23 02:43:21
# problemUrl: https://leetcode.com/problems/minimum-number-of-operations-to-sort-a-binary-tree-by-level/
# memory: 50.4 MB
# runtime: 143 ms

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        def swaps(li):
            swap = 0
            target = sorted(li)
            pos = {val: i for i, val in enumerate(li)}

            for i in range(len(li)):
                if li[i] == target[i]:
                    continue
                
                swap += 1
                li[pos[target[i]]] = li[i]
                pos[li[i]] = pos[target[i]]

            return swap

        lvl, newLvl = [root], []
        res = 0
        while lvl:
            for node in lvl:
                if node.left:
                    newLvl.append(node.left)
                if node.right:
                    newLvl.append(node.right)
            res += swaps([n.val for n in newLvl])
            lvl, newLvl = newLvl, []

        return res