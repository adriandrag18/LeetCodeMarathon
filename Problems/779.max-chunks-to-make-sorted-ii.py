# title: Max Chunks To Make Sorted II
# timestamp: 2024-12-19 11:31:18
# problemUrl: https://leetcode.com/problems/max-chunks-to-make-sorted-ii/
# memory: 18.1 MB
# runtime: 3 ms

class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        return self.helper([el[0] for el in sorted(enumerate(arr), key=lambda el: el[1])])
        

    def helper(self, arr: List[int]) -> int:
        count,  diff = 0, 0
        for i, el in enumerate(arr):
            diff += arr[i] - i
            if diff == 0:
                count += 1
        
        return count