# title: Number of Unique XOR Triplets I
# timestamp: 2025-04-16 14:06:55
# problemUrl: https://leetcode.com/problems/number-of-unique-xor-triplets-i/
# memory: 30.4 MB
# runtime: 0 ms

class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 1
        elif n == 2:
            return 2
        
        count = 0
        while n:
            n //= 2
            count += 1
        
        return 1 << count