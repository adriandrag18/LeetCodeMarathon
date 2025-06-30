# title: Find Unique Binary String
# timestamp: 2025-02-20 20:33:35
# problemUrl: https://leetcode.com/problems/find-unique-binary-string/
# memory: 17.7 MB
# runtime: 0 ms

class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n = len(nums)
        res = []
        for i in range(n):
            res.append('0' if nums[i][i] == '1' else '1')

        return ''.join(res)