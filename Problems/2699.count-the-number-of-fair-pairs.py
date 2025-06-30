# title: Count the Number of Fair Pairs
# timestamp: 2024-11-13 17:32:47
# problemUrl: https://leetcode.com/problems/count-the-number-of-fair-pairs/
# memory: 30.6 MB
# runtime: 951 ms

class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        def binSearch(l, r, target):
            while l <= r:
                m = (l + r) // 2
                if nums[m] >= target:
                    r = m -1
                else:
                    l = m + 1
            
            return r; 
        nums.sort()
        res = 0
        for i, num in enumerate(nums):
            l, u = lower - num, upper - num
            ui = binSearch(i + 1, len(nums) - 1, u + 1)
            li = binSearch(i + 1, len(nums) - 1, l)
            res += ui - li
        
        return res
