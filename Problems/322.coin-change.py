# title: Coin Change
# timestamp: 2025-05-22 16:19:48
# problemUrl: https://leetcode.com/problems/coin-change/
# memory: 18.8 MB
# runtime: 417 ms

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        
        coins = [coin for coin in coins if coin <= amount]
        # map = {coin: 1 for coin in coins}

        # def func(amount):
        #     if amount in map:
        #         return map[amount]
        #     res = min([float('inf')] + [func(amount - coin) for coin in coins if amount - coin > 0]) + 1
        #     map[amount] = res
        #     return res

        # res = func(amount)
        # print(map)
        # return res if res != float('inf') else -1

        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        for coin in coins:
            dp[coin] = 1
        
        for i in range(1, amount + 1):
            pos = []
            for coin in coins:
                if i < coin:
                    continue
                pos.append(dp[i - coin])
            if pos:
                dp[i] = min(pos) + 1
        print(dp)
        return dp[amount] if dp[amount] != float('inf') else -1