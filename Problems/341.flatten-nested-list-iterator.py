# title: Flatten Nested List Iterator
# timestamp: 2025-05-13 16:35:49
# problemUrl: https://leetcode.com/problems/flatten-nested-list-iterator/
# memory: 20.5 MB
# runtime: 57 ms

# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.stack = [[nestedList, 0]]
    
    def next(self) -> int:
        self.hasNext()
        l, i = self.stack[-1]
        res = l[i].getInteger()
        self.stack[-1][1] += 1
        
        return res
    
    def hasNext(self) -> bool:
        s = self.stack
        while s:
            l, i = s[-1]
            if i == len(l):
                s.pop()
                continue
            if l[i].isInteger():
                return True
            
            l = l[i].getList()
            s[-1][1] += 1
            s.append([l, 0])

            
        return False
         

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())