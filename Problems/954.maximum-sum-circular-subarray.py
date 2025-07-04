# title: Maximum Sum Circular Subarray
# timestamp: 2025-06-09 14:57:12
# problemUrl: https://leetcode.com/problems/maximum-sum-circular-subarray/
# memory: 21.1 MB
# runtime: 91 ms

class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        n = len(nums)
        curr, maxSum = 0, nums[0]
        currMin, minSum = 0, 0
        totalSum = 0
        for num in nums:
            curr = max(curr, 0) + num
            maxSum = max(maxSum, curr)

            currMin = min(currMin, 0) + num
            minSum = min(minSum, currMin)

            totalSum += num
        
        if maxSum < 0:
            return maxSum
            
        return max(maxSum, totalSum - minSum)
            