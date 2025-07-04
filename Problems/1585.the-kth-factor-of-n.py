# title: The kth Factor of n
# timestamp: 2025-07-04 12:24:19
# problemUrl: https://leetcode.com/problems/the-kth-factor-of-n/
# memory: 17.7 MB
# runtime: 0 ms

class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        factors = [1]
        sr = None
        for i in range(2, n):
            if i * i > n:
                break
            if i * i == n:
                sr = i
                break
            if n % i == 0:
                factors.append(i)

        if k <= len(factors):
            return factors[k-1]
        
        factors.extend(([sr] if sr else []) + [n // f for f in factors[::-1]])

        if k > len(factors):
            return -1
        
        return factors[k-1]
    