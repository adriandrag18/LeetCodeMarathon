# title: Peak Index in a Mountain Array
# timestamp: 2025-06-22 11:34:10
# problemUrl: https://leetcode.com/problems/peak-index-in-a-mountain-array/
# memory: 29.6 MB
# runtime: 0 ms

class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        l, r = 0, len(arr) - 1
        while l <= r:
            m = (l + r) // 2
            if m == 0 or arr[m - 1] < arr[m]:
                l = m + 1
            else:
                r = m - 1
            
        return r