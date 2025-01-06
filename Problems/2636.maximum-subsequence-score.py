# title: Maximum Subsequence Score
# timestamp: 2025-01-06 13:23:13
# problemUrl: https://leetcode.com/problems/maximum-subsequence-score/
# memory: 40.4 MB
# runtime: 179 ms

class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        arr = sorted(zip(nums2, nums1), reverse=True)
        heap = [num1 for _, num1 in arr[:k-1]]
        heapify(heap)
        s, res = sum(heap), -1
        for num2, num1 in arr[k-1:]:
            heappush(heap, num1)
            s += num1
            while len(heap) > k:
                s -= heappop(heap)
            res = max(res, num2 * s)
        
        return res