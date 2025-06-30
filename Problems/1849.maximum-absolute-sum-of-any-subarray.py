# title: Maximum Absolute Sum of Any Subarray
# timestamp: 2025-02-26 14:50:43
# problemUrl: https://leetcode.com/problems/maximum-absolute-sum-of-any-subarray/
# memory: 28.7 MB
# runtime: 60 ms

class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        pos, neg, currPos, currNeg = 0, 0, 0, 0
        for num in nums:
            currNeg += num
            if currNeg > 0:
                currNeg = 0
            neg = min(neg, currNeg)

            currPos += num
            if currPos < 0:
                currPos = 0
            pos = max(pos, currPos)
        print(pos, neg)

        return max(-neg, pos)
            