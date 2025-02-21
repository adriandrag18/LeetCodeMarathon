# title: Find Elements in a Contaminated Binary Tree
# timestamp: 2025-02-21 11:45:41
# problemUrl: https://leetcode.com/problems/find-elements-in-a-contaminated-binary-tree/
# memory: 21.9 MB
# runtime: 30 ms

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:

    def __init__(self, root: Optional[TreeNode]):
        self.root = root
        root.val = 0

    def find(self, target: int, root: Optional[TreeNode] = None) -> bool:
        if target == 0:
            return True
        
        i = 0
        while 2 ** i - 2 < target:
            i += 1

        onRow = target - 2 ** (i - 1) + 2
        # print(onRow, end=' ')
        li = []
        for _ in range(i-1):
            li.append((onRow + 1) % 2)
            prevRow = (onRow + 1) // 2
            onRow = prevRow
            # print(onRow, end=' ')
        li.reverse()
        # print(li)

        if root == None:
            root = self.root
        
        for leftOrRight in li:
            if leftOrRight == 1:
                root = root.right
            else:
                root = root.left
            if not root:
                return False
            
        return True
        

# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)