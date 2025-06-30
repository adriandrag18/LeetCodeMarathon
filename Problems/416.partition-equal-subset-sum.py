# title: Partition Equal Subset Sum
# timestamp: 2025-05-24 15:30:54
# problemUrl: https://leetcode.com/problems/partition-equal-subset-sum/
# memory: 17.9 MB
# runtime: 323 ms

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 == 1:
            return False
        
        target = sum(nums) // 2
        
        dp = [False] * (target + 1)
        dp[0] = True
        
        for n in nums:
            for i in range(target, -1, -1):
                if not dp[i] or i + n > target:
                    continue
                    
                dp[i + n] = True
                if i + n == target:
                    return True
        
        return False
