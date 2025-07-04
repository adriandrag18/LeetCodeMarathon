# title: Sliding Window Maximum
# timestamp: 2024-11-06 01:17:49
# problemUrl: https://leetcode.com/problems/sliding-window-maximum/
# memory: 30.4 MB
# runtime: 916 ms

from sortedcontainers import SortedList
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if k >= len(nums):
            return [max(nums)]

        li = SortedList(nums[0:k])
        res = [li[-1]]
        l = 0
        for r in range(k, len(nums)):
            li.remove(nums[l])
            li.add(nums[r])
            l += 1
            res.append(li[-1])
        return res