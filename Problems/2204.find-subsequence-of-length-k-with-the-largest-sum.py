# title: Find Subsequence of Length K With the Largest Sum
# timestamp: 2025-06-28 03:27:49
# problemUrl: https://leetcode.com/problems/find-subsequence-of-length-k-with-the-largest-sum/
# memory: 18.3 MB
# runtime: 3 ms

class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        heap = [(el, i) for i, el in enumerate(nums[:k])]
        heapify(heap)
        for i in range(k, len(nums)):
            el = nums[i]
            if el > heap[0][0]:
                heappop(heap)
                heappush(heap, (el, i))
        
        return [el for el, _ in sorted(heap, key=lambda x: x[1])]