# title: Number of Ways to Form a Target String Given a Dictionary
# timestamp: 2024-12-29 22:55:57
# problemUrl: https://leetcode.com/problems/number-of-ways-to-form-a-target-string-given-a-dictionary/
# memory: 42.8 MB
# runtime: 823 ms

class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        m = max([len(s) for s in words])
        mod = 10**9 + 7

        indexMap = [[0] * 26 for _ in range(m+1)]
        for word in words:
            for i, c in enumerate(word):
                indexMap[i][ord(c) - ord('a')] += 1

        # the first row of 1's and the first column of 0's are padding so i-1 and j-1 for the base case doesn't need any special checks
        dp = [[1] * (m+1)] + [[0] * (m+1) for _ in range(len(target))]  # dp[i][j] represents how many ways to complete the targtet if i have i characters left from tarhet and i'm at index m-j in the words (I can't use chars form 0 to m-j+1)
        for i in range(1, len(target) + 1):
            for j in range(i, m + 1):
                # #(ways) = #(ways if I skip the chars at index m-j from the words list) + #(ways i can take a char forom index m-1) * #(ways I can complete the target if i took another letter)  
                dp[i][j] = (dp[i][j - 1] + dp[i - 1][j - 1] * indexMap[-j - 1][ord(target[-i]) - ord('a')]) % mod

        return dp[-1][m]