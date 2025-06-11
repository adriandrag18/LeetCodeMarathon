# title: Find Score of an Array After Marking All Elements
# timestamp: 2024-12-14 01:52:43
# problemUrl: https://leetcode.com/problems/find-score-of-an-array-after-marking-all-elements/
# memory: 36.6 MB
# runtime: 280 ms

class Solution:
    def findScore(self, nums: List[int]) -> int:
        li = sorted([(x, i) for i, x in enumerate(nums)])
        marked = [False] * (len(nums) + 2)
        score = 0
        for x, i in li:
            if marked[i + 1]:
                continue
            score += x
            marked[i] = True
            marked[i + 2] = True
        
        return score