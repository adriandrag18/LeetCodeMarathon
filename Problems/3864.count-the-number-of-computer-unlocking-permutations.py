# title: Count the Number of Computer Unlocking Permutations
# timestamp: 2025-06-08 06:16:13
# problemUrl: https://leetcode.com/problems/count-the-number-of-computer-unlocking-permutations/
# memory: 31.8 MB
# runtime: 11 ms

class Solution:
    def countPermutations(self, complexity: List[int]) -> int:
        n = len(complexity)
        minC = min(complexity)
        if complexity[0] != minC:
            return 0
        if complexity.count(minC) != 1:
            return 0
        
        prod = 1
        for j in range(2, n):
            prod = prod * j % (10**9 + 7)
        return prod