# title: Max Chunks To Make Sorted
# timestamp: 2024-12-19 11:30:55
# problemUrl: https://leetcode.com/problems/max-chunks-to-make-sorted/
# memory: 17.7 MB
# runtime: 0 ms

class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        return list(accumulate(x-i for i, x in enumerate(arr))).count(0)