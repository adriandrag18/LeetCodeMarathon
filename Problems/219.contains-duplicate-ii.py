# title: Contains Duplicate II
# timestamp: 2025-06-12 12:10:24
# problemUrl: https://leetcode.com/problems/contains-duplicate-ii/
# memory: 36.7 MB
# runtime: 26 ms

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        map = {}
        for i, num in enumerate(nums):
            if num in map and i - map[num] <= k:
                return True
            map[num] = i

        return False