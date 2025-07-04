# title: Number of Unique XOR Triplets II
# timestamp: 2025-04-16 14:32:34
# problemUrl: https://leetcode.com/problems/number-of-unique-xor-triplets-ii/
# memory: 18.2 MB
# runtime: 9024 ms

class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        n = len(nums)
        # print(n)
        seen = set()
        for i in range(n-1, -1, -1):
            for j in range(i, n):
                seen.add(nums[i] ^ nums[j])
            
        res = set()
        for i in range(n):
            for el in seen:
                res.add(nums[i] ^ el)

        return len(res)