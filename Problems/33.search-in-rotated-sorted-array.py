# title: Search in Rotated Sorted Array
# timestamp: 2024-12-12 18:23:35
# problemUrl: https://leetcode.com/problems/search-in-rotated-sorted-array/
# memory: 17.6 MB
# runtime: 0 ms

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def getRotation():
            last = nums[-1]
            if nums[0] < last:
                return 0

            l, r = 0, len(nums) - 2
            while l <= r:
                m = (l + r) // 2
                if nums[m] > last:
                    l = m + 1
                    continue
                r = m - 1
            
            return r + 1
        
        rot = getRotation()
        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            if nums[m + rot - len(nums)] == target:
                return (m + rot) % len(nums)
            if nums[m + rot - len(nums)] < target:
                l = m + 1
                continue
            r = m - 1
        
        return -1