# title: Find K Pairs with Smallest Sums
# timestamp: 2025-06-21 20:06:37
# problemUrl: https://leetcode.com/problems/find-k-pairs-with-smallest-sums/
# memory: 34.8 MB
# runtime: 79 ms

class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        heap = []
        nums1 = nums1[:k]
        n1, n2 = len(nums1), len(nums2)
        for i in range(n1):
            heappush(heap, (nums1[i] + nums2[0], i, 0))

        res = []
        while k:
            s, i, j = heappop(heap)
            res.append((nums1[i], nums2[j]))
            if j + 1 < n2:
                heappush(heap, (nums1[i] + nums2[j+1], i, j + 1))
            k -= 1
        
        return res
            
