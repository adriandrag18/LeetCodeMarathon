# title: Count of Matches in Tournament
# timestamp: 2025-06-01 20:57:59
# problemUrl: https://leetcode.com/problems/count-of-matches-in-tournament/
# memory: 17.8 MB
# runtime: 42 ms

class Solution:
    def numberOfMatches(self, n: int) -> int:
        total = 0
        while n > 1:
            total += n // 2
            n = (n + 1) // 2
        
        return total