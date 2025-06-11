# title: Final Prices With a Special Discount in a Shop
# timestamp: 2024-12-19 01:25:25
# problemUrl: https://leetcode.com/problems/final-prices-with-a-special-discount-in-a-shop/
# memory: 17.7 MB
# runtime: 4 ms

class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        for i, price in enumerate(prices):
            j = i + 1
            while j < len(prices) and price < prices[j]: j += 1
            if not j == len(prices):
                prices[i] -= prices[j]
        
        return prices