# title: Coin Change II
# timestamp: 2025-05-24 15:48:52
# problemUrl: https://leetcode.com/problems/coin-change-ii/
# memory: 18.1 MB
# runtime: 116 ms

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        if amount == 0:
            return 1
        
        coins = [coin for coin in coins if coin <= amount]

        dp = [0] * (amount + 1)
        dp[0] = 1
        
        for coin in coins:
            for i in range(coin, amount + 1):
                dp[i] += dp[i - coin]
        
        return dp[amount]