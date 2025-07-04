# title: Minimum Operations to Convert All Elements to Zero
# timestamp: 2025-06-09 02:43:08
# problemUrl: https://leetcode.com/problems/minimum-operations-to-convert-all-elements-to-zero/
# memory: 29.8 MB
# runtime: 198 ms

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        stack = []
        res = 0
        for num in nums:
            while stack and stack[-1] > num:
                stack.pop()
            if not stack or stack[-1] < num:
                if num == 0:
                    continue
                res += 1
                stack.append(num)
            
        return res