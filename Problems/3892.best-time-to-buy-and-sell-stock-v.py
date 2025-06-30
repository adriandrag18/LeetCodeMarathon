# title: Best Time to Buy and Sell Stock V
# timestamp: 2025-06-08 00:12:19
# problemUrl: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-v/
# memory: 18.4 MB
# runtime: 2306 ms

class Solution:
    def maximumProfit(self, prices: List[int], k: int) -> int:
        n = len(prices)
        if n < 2:
            return 0
        # MAX = 10**10
        # prev = [[-MAX] * 3 for _ in range(k + 1)]
        # prev[0] = [0, -prices[0], prices[0]]

        # for i in range(1, n):
        #     curr = [[-MAX] * 3 for _ in range(k + 1)]
        #     for t in range(k + 1):
        #         curr[t][0] = prev[t][0]
        #         if t > 1:
        #             curr[t][0] = max([curr[t][0], prev[t - 1][1] + prices[i], prev[t - 1][2] - prices[i]])

        #         curr[t][1] = max(prev[t][1], prev[t][0] - prices[i])
        #         curr[t][2] = max(prev[t][2], prev[t][0] + prices[i])

        #     prev = curr
        #     print(prev)

        # return max([prev[t][0] for t in range(k + 1)])
        prev = [[0, -prices[0], prices[0]] for _ in range(k + 1)]

        for i in range(1, n):
            curr = [[0, -float('inf'), -float('inf')] for _ in range(k + 1)]
            for j in range(k):
                curr[j][0] = max([prev[j][0], prev[j][1] + prices[i], prev[j][2] - prices[i]])
                curr[j][1] = max(prev[j][1], prev[j+1][0] - prices[i])
                curr[j][2] = max(prev[j][2], prev[j+1][0] + prices[i])
            prev = curr

        return max([el[0] for el in prev])