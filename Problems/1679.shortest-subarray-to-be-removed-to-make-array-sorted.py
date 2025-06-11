# title: Shortest Subarray to be Removed to Make Array Sorted
# timestamp: 2024-11-15 23:48:58
# problemUrl: https://leetcode.com/problems/shortest-subarray-to-be-removed-to-make-array-sorted/
# memory: 30.2 MB
# runtime: 12 ms

class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        if len(arr) < 2:
            return 0

        l = 1
        while l < len(arr) and arr[l-1] <= arr[l]:
            l += 1
        if l == len(arr):
            return 0
        
        r = len(arr) -  1
        while r > 0 and arr[r-1] <= arr[r]:
            r -= 1
        
        result = min(len(arr) - l, r)
        
        i, j = 0, r
        while i < l and j < len(arr):
            if arr[i] <= arr[j]:
                i += 1
                result = min(result, j - i)
                continue
            j += 1

        return result