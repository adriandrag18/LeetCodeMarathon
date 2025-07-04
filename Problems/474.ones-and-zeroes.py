# title: Ones and Zeroes
# timestamp: 2025-06-11 00:24:53
# problemUrl: https://leetcode.com/problems/ones-and-zeroes/
# memory: 18 MB
# runtime: 574 ms

class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        dp = [[-1] * (n + 1) for _ in range(m + 1)]
        dp[0][0] = 0
        for s in strs:
            # print(s)
            ones = s.count('1')
            zeroes = len(s) - ones
            for i in range(m - zeroes, -1, -1):
                for j in range(n - ones, -1, -1):
                    if dp[i][j] == -1:
                        continue
                    dp[i + zeroes][j + ones] = max(dp[i + zeroes][j + ones], dp[i][j] + 1)
            # print(*dp, sep = '\n')
            
        return max([max(line) for line in dp])
