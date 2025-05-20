# title: Single Number
# timestamp: 2025-05-20 11:12:13
# problemUrl: https://leetcode.com/problems/single-number/
# memory: 19.9 MB
# runtime: 7 ms

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        counter = Counter(nums)
        for n, i in counter.items():
            if i == 1:
                return n
        
        return -1
