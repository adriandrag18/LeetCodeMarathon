# title: Binary Search Tree Iterator
# timestamp: 2025-06-18 17:36:05
# problemUrl: https://leetcode.com/problems/binary-search-tree-iterator/
# memory: 25.1 MB
# runtime: 15 ms

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.root = root
        while root.left:
            root = root.left
        self._next = root
        self.last = None

    def _searchNext(self, target, root):
        if target == root.val:
            if root.right:
                root = root.right
                while root.left:
                    root = root.left
                return root, False
            else:
                return None, True
        if target < root.val:
            next, needNext = self._searchNext(target, root.left)
            if not next and needNext:
                return root, False
            return next, needNext
        else:
            return self._searchNext(target, root.right)

    def next(self) -> int:
        if self._next:
            self._next, self.last = None, self._next
            return self.last.val
        
        self.last, _ = self._searchNext(self.last.val, self.root)
        return self.last.val
        

    def hasNext(self) -> bool:
        if self._next:
            return True
        
        self._next, flag = self._searchNext(self.last.val, self.root)
        if flag:
            self._next = None
        
        return not flag

# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()