# title: Inverse Coin Change
# timestamp: 2025-06-22 06:09:32
# problemUrl: https://leetcode.com/problems/inverse-coin-change/
# memory: 17.8 MB
# runtime: 15 ms

class Solution:
    def findCoins(self, numWays: List[int]) -> List[int]:
        n = len(numWays)
        coins = []
        dp = [0] * (n + 1)
        dp[0] = 1

        for i, ways in enumerate(numWays):
            if ways == dp[i+1]:
                continue
                
            if ways - 1 != dp[i+1]:
                print('More then 1:', i, ways, dp[i])
                return []
            
            coins.append(i + 1)
            
            for j in range(n - i):
                dp[i + 1 + j] += dp[j]

            print(i, dp)

        return coins
            