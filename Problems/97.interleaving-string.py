# title: Interleaving String
# timestamp: 2025-06-15 15:07:14
# problemUrl: https://leetcode.com/problems/interleaving-string/
# memory: 17.7 MB
# runtime: 48 ms

class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        n1, n2, n3 = len(s1), len(s2), len(s3)
        if n1 + n2 != n3:
            return False
        
        prev = dp = [True] + [False] * n1

        startJ = 0
        for i in range(n2 + 1):
            for j in range(startJ, n1 + 1):
                if i == 0 and j == 0:
                    continue
                dp[j] = (j > 0 and s1[j - 1] == s3[i + j - 1] and dp[j - 1]) or (i > 0 and s2[i - 1] == s3[i + j - 1] and prev[j])
                if j == startJ and not dp[j]:
                    startJ += 1
            
            
            prev, dp = dp, [False] * (n1 + 1)
        
        return prev[-1]