# title: Maximum Number of Consecutive Values You Can Make
# timestamp: 2025-06-01 20:39:37
# problemUrl: https://leetcode.com/problems/maximum-number-of-consecutive-values-you-can-make/
# memory: 22 MB
# runtime: 53 ms

class Solution:
    def getMaximumConsecutive(self, coins: List[int]) -> int:
        coins.sort()

        max = 1
        for coin in coins:
            if coin > max: break
            max += coin
            
        return max
        