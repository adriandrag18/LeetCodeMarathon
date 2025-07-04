# title: Maximum Difference Between Even and Odd Frequency I
# timestamp: 2025-06-10 19:06:19
# problemUrl: https://leetcode.com/problems/maximum-difference-between-even-and-odd-frequency-i/
# memory: 17.9 MB
# runtime: 3 ms

class Solution:
    def maxDifference(self, s: str) -> int:
        counter = Counter(s)
        b = max([c for c in counter.values() if c % 2 == 1])
        c = min([c for c in counter.values() if c % 2 == 0])

        return b - c