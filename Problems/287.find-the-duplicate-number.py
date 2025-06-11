# title: Find the Duplicate Number
# timestamp: 2024-12-19 16:27:07
# problemUrl: https://leetcode.com/problems/find-the-duplicate-number/
# memory: 30.1 MB
# runtime: 19 ms

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = nums[nums[0]], nums[nums[nums[0]]]
        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]
        
        slow2 = nums[0]
        while slow != slow2:
            slow = nums[slow]
            slow2 = nums[slow2]
        
        return slow
