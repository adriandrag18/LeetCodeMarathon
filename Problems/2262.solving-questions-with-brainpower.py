# title: Solving Questions With Brainpower
# timestamp: 2025-06-05 12:25:58
# problemUrl: https://leetcode.com/problems/solving-questions-with-brainpower/
# memory: 56.9 MB
# runtime: 85 ms

class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)
        dp = [0] * (n + 1)

        for i in range(n):
            points, power = questions[n - i - 1]
            dp[i + 1] = max(dp[i], dp[max(i - power, 0)] + points)
        
        return dp[-1]