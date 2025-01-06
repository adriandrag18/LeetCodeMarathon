# title: Majority Element
# timestamp: 2025-01-06 11:14:58
# problemUrl: https://leetcode.com/problems/majority-element/
# memory: 19.3 MB
# runtime: 6 ms

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        
        for el, count in freq.items():
            if count >= len(nums) / 2:
               return el 
