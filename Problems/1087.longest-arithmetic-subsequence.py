# title: Longest Arithmetic Subsequence
# timestamp: 2025-06-30 01:09:22
# problemUrl: https://leetcode.com/problems/longest-arithmetic-subsequence/
# memory: 106.2 MB
# runtime: 4998 ms

class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        map = {}
        for num in nums:
            for dif in range(-500, 501):
                map[(num + dif, dif)] = map.get((num, dif), 0) + 1
        
        return max(map.values())
