# title: Best Time to Buy and Sell Stock III
# timestamp: 2025-06-24 15:29:31
# problemUrl: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/
# memory: 28.8 MB
# runtime: 332 ms

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [[0, -prices[0]], [0, -prices[0]]]
        for i in range(1, n):
            dp[0][0] = max(dp[0][0], dp[0][1] + prices[i])
            dp[0][1] = max(dp[0][1], dp[1][0] - prices[i])
            dp[1][0] = max(dp[1][0], dp[1][1] + prices[i])
            dp[1][1] = max(dp[1][1], -prices[i])
            
        return max([el[0] for el in dp])