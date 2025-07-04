# title: Longest Harmonious Subsequence
# timestamp: 2025-06-30 10:04:09
# problemUrl: https://leetcode.com/problems/longest-harmonious-subsequence/
# memory: 19.3 MB
# runtime: 19 ms

class Solution:
    def findLHS(self, nums: List[int]) -> int:
        counter = Counter(nums)
        res = 0
        for num, count in counter.items():
            if num + 1 in counter:
                res = max(res, counter[num + 1] + count)
        
        return res