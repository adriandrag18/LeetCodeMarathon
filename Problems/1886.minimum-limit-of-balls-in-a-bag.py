# title: Minimum Limit of Balls in a Bag
# timestamp: 2024-12-07 18:10:26
# problemUrl: https://leetcode.com/problems/minimum-limit-of-balls-in-a-bag/
# memory: 29.3 MB
# runtime: 560 ms

class Solution:
    def minimumSize(self, nums: List[int], maxOps: int) -> int:
        low, high = 1, max(nums)

        while low < high:
            mid = (low + high) // 2
            if sum((n - 1) // mid for n in nums) <= maxOps: 
                high = mid
                continue
            low = mid + 1
        
        return high