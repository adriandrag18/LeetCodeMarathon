# title: Median of Two Sorted Arrays
# timestamp: 2025-01-12 04:24:33
# problemUrl: https://leetcode.com/problems/median-of-two-sorted-arrays/
# memory: 18.1 MB
# runtime: 3 ms

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            return self.findMedianSortedArrays(nums2, nums1)
        
        nums1 = [-10**9] + nums1 + [10**9]
        nums2 = [-10**9] + nums2 + [10**9]
        n1, n2 = len(nums1), len(nums2)
        n = n1 + n2
        l, r = 0, n1 - 1
        while l <= r:
            m = (l + r) // 2
            m2 = n // 2 - m - 2
            if nums1[m] <= nums2[m2 + 1] and nums2[m2] <= nums1[m + 1]:
                break
            if nums1[m] > nums2[m2 + 1]:
                r = m - 1
                continue
            l = m + 1
        
        med = min(nums1[m + 1], nums2[m2 + 1])
        if n % 2 == 0:
            med = (med + max(nums1[m], nums2[m2])) / 2
        
        return med