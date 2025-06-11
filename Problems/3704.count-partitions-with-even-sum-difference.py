# title: Count Partitions with Even Sum Difference
# timestamp: 2025-01-31 14:54:58
# problemUrl: https://leetcode.com/problems/count-partitions-with-even-sum-difference/
# memory: 17.9 MB
# runtime: 0 ms

class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        return len(nums) - 1 if sum(nums) % 2 == 0 else 0