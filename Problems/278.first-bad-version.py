# title: First Bad Version
# timestamp: 2025-06-18 17:57:17
# problemUrl: https://leetcode.com/problems/first-bad-version/
# memory: 17.7 MB
# runtime: 30 ms

# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        l, r = 1, n
        while l <= r:
            m = (l + r) // 2
            if isBadVersion(m):
                r = m - 1
            else:
                l = m + 1
        return l