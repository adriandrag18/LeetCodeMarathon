# title: Best Time to Buy and Sell Stock II
# timestamp: 2025-01-07 21:07:24
# problemUrl: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/
# memory: 18.9 MB
# runtime: 0 ms

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy, profit = prices[0], 0
        for price in prices[1:]:
            if price > buy:
                profit += price - buy
            buy = price
        
        return profit