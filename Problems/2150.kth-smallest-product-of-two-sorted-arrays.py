# title: Kth Smallest Product of Two Sorted Arrays
# timestamp: 2025-06-25 23:33:00
# problemUrl: https://leetcode.com/problems/kth-smallest-product-of-two-sorted-arrays/
# memory: 25.6 MB
# runtime: 3217 ms

class Solution:
    def kthSmallestProduct(self, nums1: List[int], nums2: List[int], k: int) -> int:
        def func(v):
            count = 0
            for x1 in nums1:
                if x1 > 0:
                    count += bisect_right(nums2, v // x1)
                elif x1 < 0:
                    count += len(nums2) - bisect_left(nums2, -(-v // x1))
                else:
                    count += len(nums2) if v >= 0 else 0
                
            return count

        n1 = len(nums1)
        left, right = -(10**10), 10**10
        while left <= right:
            mid = (left + right) // 2
            if func(mid) < k:
                left = mid + 1
            else:
                right = mid - 1
        return left