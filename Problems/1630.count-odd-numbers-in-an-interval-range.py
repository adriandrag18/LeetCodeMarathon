# title: Count Odd Numbers in an Interval Range
# timestamp: 2025-06-12 20:39:48
# problemUrl: https://leetcode.com/problems/count-odd-numbers-in-an-interval-range/
# memory: 17.5 MB
# runtime: 35 ms

class Solution:
    def countOdds(self, low: int, high: int) -> int:
        diff = high - low
        if diff % 2 == 1:
            return (diff + 1) // 2
        if low % 2 == 1:
            return diff // 2 + 1
        return diff // 2