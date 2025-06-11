# title: 4Sum II
# timestamp: 2025-01-09 17:22:13
# problemUrl: https://leetcode.com/problems/4sum-ii/
# memory: 18.2 MB
# runtime: 358 ms

class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        res, map = 0, {}
        for a in nums3:
            for b in nums4:
                map[a+b] = map.get(a + b, 0) + 1
        
        for a in Counter(nums1).items():
            for b in Counter(nums2).items():
                res += map.get(-a[0] - b[0], 0) * a[1] * b[1]
                
        return res
