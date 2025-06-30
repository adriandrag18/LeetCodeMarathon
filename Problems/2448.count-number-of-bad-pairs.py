# title: Count Number of Bad Pairs
# timestamp: 2025-02-10 01:00:28
# problemUrl: https://leetcode.com/problems/count-number-of-bad-pairs/
# memory: 38.9 MB
# runtime: 74 ms

class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        freq = {}
        good_pairs = 0

        for i, num in enumerate(nums):
            key = num - i
            good_pairs += freq.get(key, 0)
            freq[key] = freq.get(key, 0) + 1

        n = len(nums)
        return (n * (n - 1)) // 2 - good_pairs