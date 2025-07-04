# title: Best Time to Buy and Sell Stock with Cooldown
# timestamp: 2025-06-24 15:42:57
# problemUrl: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/
# memory: 18 MB
# runtime: 3 ms

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        curr, prev, prev2 = [0, -prices[0]], [0, -prices[0]], 0
        for i in range(1, n):
            curr[1] = max(prev[1], prev2 - prices[i])
            curr[0] = max(prev[0], prev[1] + prices[i])
            curr, prev, prev2 = [0, 0], curr, prev[0]
        
        return max(prev)
