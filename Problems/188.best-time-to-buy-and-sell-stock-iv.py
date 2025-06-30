# title: Best Time to Buy and Sell Stock IV
# timestamp: 2025-06-07 23:45:48
# problemUrl: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/
# memory: 17.8 MB
# runtime: 55 ms

class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        dp = [[0, -prices[0]] for _ in range(k + 1)]

        for i in range(1, n):
            for j in range(k):
                dp[j][0] = max(dp[j][0], dp[j][1] + prices[i])
                dp[j][1] = max(dp[j][1], dp[j+1][0] - prices[i])

        return max([el[0] for el in dp])