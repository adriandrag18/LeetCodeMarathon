# title: K-th Smallest in Lexicographical Order
# timestamp: 2025-06-09 11:32:35
# problemUrl: https://leetcode.com/problems/k-th-smallest-in-lexicographical-order/
# memory: 17.7 MB
# runtime: 1 ms

class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        def countSteps(i, j):
            steps = 0
            while i <= n:
                steps += min(j, n + 1) - i
                i *= 10
                j *= 10
            return steps
        
        curr = 1
        k -= 1

        while k > 0:
            steps = countSteps(curr, curr + 1)
            if steps <= k:
                curr += 1
                k -= steps
            else:
                curr *= 10
                k -= 1
        
        return curr
        
            