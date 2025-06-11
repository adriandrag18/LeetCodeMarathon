# title: Contains Duplicate
# timestamp: 2024-11-26 02:00:00
# problemUrl: https://leetcode.com/problems/contains-duplicate/
# memory: 30.6 MB
# runtime: 17 ms

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return not len(set(nums)) == len(nums)