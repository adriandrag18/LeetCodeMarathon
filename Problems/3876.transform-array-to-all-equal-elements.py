# title: Transform Array to All Equal Elements
# timestamp: 2025-06-08 05:55:52
# problemUrl: https://leetcode.com/problems/transform-array-to-all-equal-elements/
# memory: 22.7 MB
# runtime: 98 ms

class Solution:
    def canMakeEqual(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        if n < 2:
            return True

        for target in [-1, 1]:
            if (n - nums.count(target)) % 2 == 1:
                continue
            flip = [False] * n
            flip[0] = nums[0] != target
            count = 1 if flip[0] else 0
            for i in range(1, n):
                flip[i] = flip[i-1] if nums[i] == target else not flip[i-1]
                if flip[i] and i < n - 1:
                    count += 1
            
            if count <= k and not flip[-1]:
                return True
        
        return False
