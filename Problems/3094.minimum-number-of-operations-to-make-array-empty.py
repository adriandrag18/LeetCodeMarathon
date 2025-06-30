# title: Minimum Number of Operations to Make Array Empty
# timestamp: 2025-06-01 21:10:06
# problemUrl: https://leetcode.com/problems/minimum-number-of-operations-to-make-array-empty/
# memory: 35.5 MB
# runtime: 23 ms

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        counter = Counter(nums)
        total = 0
        for el in counter.values():
            if el == 1:
                return -1
            total += (el + 2) // 3
        
        return total