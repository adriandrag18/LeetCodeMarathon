# title: Delete and Earn
# timestamp: 2025-06-06 18:11:12
# problemUrl: https://leetcode.com/problems/delete-and-earn/
# memory: 19.5 MB
# runtime: 7 ms

class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        n = max(nums)
        dp = [0 for _ in range(n)]
        for num in nums:
            dp[num - 1] += num
            
        taken, notTaken = dp[0], 0
        for i in range(1, n):
            taken, notTaken = notTaken + dp[i], max(taken, notTaken)
        
        return max(taken, notTaken)
