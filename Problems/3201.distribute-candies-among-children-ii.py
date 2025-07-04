# title: Distribute Candies Among Children II
# timestamp: 2025-06-01 19:32:31
# problemUrl: https://leetcode.com/problems/distribute-candies-among-children-ii/
# memory: 17.6 MB
# runtime: 1395 ms

class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        if n > 3 * limit:
            return 0
        
        res = 0
        for i in range(min(n, limit) + 1):
            remaining = n - i
            # print(res, remaining)
            if remaining > 2 * limit:
                continue
            if remaining >= limit:
                res += 2 * limit - remaining + 1
                continue
            res += remaining + 1
        # print(res, remaining)   

        if n <= limit:
            return (n + 2) * (n + 1) // 2
        
        return res