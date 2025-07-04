# title: Binary Search
# timestamp: 2024-11-14 12:28:39
# problemUrl: https://leetcode.com/problems/binary-search/
# memory: 17.6 MB
# runtime: 0 ms

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 0:
            return -1

        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if target == nums[mid]:
                return mid
            if target < nums[mid]:
                r = mid - 1
                continue
            l = mid + 1
        
        return -1