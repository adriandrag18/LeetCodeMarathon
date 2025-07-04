# title: Final Array State After K Multiplication Operations I
# timestamp: 2024-12-16 08:09:04
# problemUrl: https://leetcode.com/problems/final-array-state-after-k-multiplication-operations-i/
# memory: 17.2 MB
# runtime: 13 ms

class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        for i in range(k):
            arr = sorted([[x, i] for i, x in enumerate(nums)])
            nums[arr[0][1]] = arr[0][0] * multiplier
        
        return nums