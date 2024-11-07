# title: Best Time to Buy and Sell Stock
# timestamp: 2024-11-07 14:45:37
# problemUrl: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
# memory: 26 MB
# runtime: 114 ms

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # n = len(p)
        # dp = [p[n-1]] * n
        # for i in range(n-2, -1, -1):
        #     dp[i] = max(dp[i+1], p[i])

        # res = 0
        # for i in range(n):
        #     res = max(dp[i] - p[i], res)
        
        if len(prices) < 2:
            return 0

        maxProfit = 0
        bestBuySoFar = prices[0]
        for price in prices[1:]:
            maxProfit = max(maxProfit, price - bestBuySoFar)
            bestBuySoFar = min(bestBuySoFar, price)

        return maxProfit