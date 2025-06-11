# title: Generate Parentheses
# timestamp: 2024-11-08 04:07:09
# problemUrl: https://leetcode.com/problems/generate-parentheses/
# memory: 17 MB
# runtime: 0 ms

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        dp = {1: set(['()'])}
        for i in range(2, n+1):
            dp[i] = {'(' + s + ')' for s in dp[i-1]}
            for j in range(1, i):
                dp[i].update({si + sj for si in dp[i-j] for sj in dp[j]})

        return list(dp[n])
