# title: Number of Sub-arrays With Odd Sum
# timestamp: 2025-02-26 15:42:11
# problemUrl: https://leetcode.com/problems/number-of-sub-arrays-with-odd-sum/
# memory: 22 MB
# runtime: 42 ms

class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        mod = 10**9 + 7
        prefix, oddCount = 0, 0
        for num in arr:
            prefix += num
            oddCount += prefix % 2
        
        return (len(arr) - oddCount + 1) * oddCount % mod
