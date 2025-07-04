# title: Kth Largest Element in an Array
# timestamp: 2025-01-02 18:43:55
# problemUrl: https://leetcode.com/problems/kth-largest-element-in-an-array/
# memory: 28.7 MB
# runtime: 50 ms

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return sorted(nums)[len(nums) - k]
        # heapq.heapify(nums)
        # while len(nums) > k:
        #     heapq.heappop(nums)
        
        # return nums[0]