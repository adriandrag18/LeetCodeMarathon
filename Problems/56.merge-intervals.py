# title: Merge Intervals
# timestamp: 2025-01-10 07:00:49
# problemUrl: https://leetcode.com/problems/merge-intervals/
# memory: 21.1 MB
# runtime: 12 ms

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = []
        prev = intervals[0]
        for interval in intervals[1:]:
            if interval[0] <= prev[1]:
                prev[1] = max(prev[1], interval[1])
                continue
            res.append(prev)
            prev = interval
        
        res.append(prev)
        return res