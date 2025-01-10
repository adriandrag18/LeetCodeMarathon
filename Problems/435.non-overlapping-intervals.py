# title: Non-overlapping Intervals
# timestamp: 2025-01-10 07:15:25
# problemUrl: https://leetcode.com/problems/non-overlapping-intervals/
# memory: 51.5 MB
# runtime: 67 ms

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda i: i[1])
        end = -10**9
        count = 0
        for interval in intervals:
            if end <= interval[0]:
                end = interval[1]
                continue
            count += 1
            
        return count