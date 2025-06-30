# title: Insert Interval
# timestamp: 2025-01-10 06:55:06
# problemUrl: https://leetcode.com/problems/insert-interval/
# memory: 19.8 MB
# runtime: 2 ms

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        curr = newInterval
        for i, interval in enumerate(intervals):
            if interval[1] < curr[0]:
                res.append(interval)
                continue

            if interval[0] <= curr[1]:
                curr = [min(interval[0], curr[0]), max(interval[1], curr[1])]
                continue

            res.append(curr)
            curr = None
            res.extend(intervals[i:])
            break

        if curr:
            res.append(curr)
        
        return res