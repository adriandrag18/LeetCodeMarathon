# title: H-Index
# timestamp: 2025-06-06 16:27:11
# problemUrl: https://leetcode.com/problems/h-index/
# memory: 18.2 MB
# runtime: 1 ms

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        for i, c in enumerate(sorted(citations, reverse=True)):
            if i >= c:
                return i
        
        return len(citations)