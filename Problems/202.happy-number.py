# title: Happy Number
# timestamp: 2025-05-24 14:41:09
# problemUrl: https://leetcode.com/problems/happy-number/
# memory: 17.9 MB
# runtime: 2 ms

class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while n not in seen:
            seen.add(n)
            n = sum([int(d)**2 for d in str(n)])
            if n == 1:
                return True

        return False