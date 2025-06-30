# title: Find Right Interval
# timestamp: 2025-06-16 15:55:13
# problemUrl: https://leetcode.com/problems/find-right-interval/
# memory: 22.1 MB
# runtime: 63 ms

class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        n = len(intervals)
        sortedIntervals = sorted([(interval[0], i) for i, interval in enumerate(intervals)])
        res = [-1] * n

        def binSearch(target):
            l, r = 0, n - 1
            while l <= r:
                m = (l + r) // 2
                start, i = sortedIntervals[m]
                if start == target:
                    return i
                if start < target:
                    l = m + 1
                else:
                    r = m - 1
            
            return sortedIntervals[l][1] if l != n else -1

        for i, (_, end) in enumerate(intervals):
            res[i] = binSearch(end)
        
        return res