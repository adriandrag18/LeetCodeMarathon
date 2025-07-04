# title: Minimum Operations to Make Array Sum Divisible by K
# timestamp: 2025-04-16 13:40:17
# problemUrl: https://leetcode.com/problems/minimum-operations-to-make-array-sum-divisible-by-k/
# memory: 18.1 MB
# runtime: 1 ms

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        return sum(nums) % k