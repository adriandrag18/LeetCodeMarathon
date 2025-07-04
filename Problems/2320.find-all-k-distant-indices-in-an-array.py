# title: Find All K-Distant Indices in an Array
# timestamp: 2025-06-24 13:16:31
# problemUrl: https://leetcode.com/problems/find-all-k-distant-indices-in-an-array/
# memory: 18.1 MB
# runtime: 0 ms

class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        n = len(nums)
        res = []
        r = 0
        for j in range(n):
            if nums[j] != key:
                continue
            
            l = max(r, j - k)
            r = min(n - 1, j + k) + 1
            for i in range(l, r):
                res.append(i)
            
        return res