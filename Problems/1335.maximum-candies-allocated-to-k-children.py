# title: Maximum Candies Allocated to K Children
# timestamp: 2025-03-14 11:37:42
# problemUrl: https://leetcode.com/problems/maximum-candies-allocated-to-k-children/
# memory: 29.6 MB
# runtime: 135 ms

class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        # sort(candies)
        def helper(n):
            count = 0
            
            for el in candies:
                count += el // n
            
            # print(n, count >= k)
            return count >= k

        l, r = 1, sum(candies) // k + 1
        # print(l, r)
        while l <= r:
            m = (l + r) // 2
            if helper(m):
                l = m + 1 
            else:
                r = m - 1
        
        return r