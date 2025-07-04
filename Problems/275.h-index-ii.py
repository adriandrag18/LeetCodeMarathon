# title: H-Index II
# timestamp: 2025-06-19 13:20:01
# problemUrl: https://leetcode.com/problems/h-index-ii/
# memory: 23 MB
# runtime: 0 ms

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        citations.reverse()

        l, r = 0, n - 1
        while l <= r:
            m = (l + r) // 2
            if citations[m] == m + 1:
                return m + 1
            if citations[m] > m + 1:
                l = m + 1
            else:
                r = m - 1
        
        return l