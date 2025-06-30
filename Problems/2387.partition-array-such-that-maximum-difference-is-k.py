# title: Partition Array Such That Maximum Difference Is K
# timestamp: 2025-06-19 12:44:28
# problemUrl: https://leetcode.com/problems/partition-array-such-that-maximum-difference-is-k/
# memory: 29.1 MB
# runtime: 74 ms

class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        if not nums:
            return 0
        
        n = len(nums)
        nums.sort()
        count = 1
        next = nums[0] + k
        for num in nums:
            if num > next:
                next = num + k
                count += 1
        
        return count