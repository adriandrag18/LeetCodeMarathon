# title: Make Array Elements Equal to Zero
# timestamp: 2024-11-17 04:58:32
# problemUrl: https://leetcode.com/problems/make-array-elements-equal-to-zero/
# memory: 16.5 MB
# runtime: 3650 ms

class Solution:
    def countValidSelections(self, nums: List[int]) -> int:
        n = len(nums)
        res = 0
        for curr in range(n):
            if nums[curr] != 0:
                continue
            for step in [-1, 1]:
                arr = nums[:]
                currI, stepI = curr, step
                # print(curr, step, arr, currI, stepI)
                while 0 <= currI < n:
                    if arr[currI] == 0:
                        currI += stepI
                        continue
                    arr[currI] -= 1
                    stepI *= -1
                    # if arr[currI] == 0:
                        # print(curr, step, arr, currI, step)
                    currI += stepI
                if max(arr) == 0:
                    # print(curr, step)
                    res += 1
        return res