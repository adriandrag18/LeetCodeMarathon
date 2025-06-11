# title: Increasing Triplet Subsequence
# timestamp: 2024-12-28 19:59:14
# problemUrl: https://leetcode.com/problems/increasing-triplet-subsequence/
# memory: 37.5 MB
# runtime: 14 ms

class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        min1, min2 = 100000000000, 10000000000
        for n in nums:
            if n <= min1:
                min1 = n
                continue
            if n <= min2:
                min2 = n
                continue
            return True
        
        return False