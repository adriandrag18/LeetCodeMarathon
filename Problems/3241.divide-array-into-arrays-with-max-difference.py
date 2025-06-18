# title: Divide Array Into Arrays With Max Difference
# timestamp: 2025-06-18 12:52:07
# problemUrl: https://leetcode.com/problems/divide-array-into-arrays-with-max-difference/
# memory: 33.4 MB
# runtime: 84 ms

class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums.sort()
        res = []
        for i in range(0, len(nums), 3):
            if nums[i + 2] - nums[i] <= k:
                res.append(nums[i:i+3])
            else:
                return []
        
        return res
