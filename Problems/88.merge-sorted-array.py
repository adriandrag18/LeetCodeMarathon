# title: Merge Sorted Array
# timestamp: 2025-01-04 01:18:59
# problemUrl: https://leetcode.com/problems/merge-sorted-array/
# memory: 17.9 MB
# runtime: 0 ms

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i, j, k = m - 1, n - 1, m + n
        while j >= 0 and i >= 0:
            k -= 1
            if nums1[i] < nums2[j]:
                nums1[k] = nums2[j]
                j -= 1
                continue
            nums1[k] = nums1[i]
            i -= 1
        
        while j >= 0:
            k -= 1
            nums1[k] = nums2[j]
            j -= 1
        