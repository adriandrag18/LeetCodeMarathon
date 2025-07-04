# title: Next Greater Element II
# timestamp: 2025-05-13 15:41:36
# problemUrl: https://leetcode.com/problems/next-greater-element-ii/
# memory: 19.4 MB
# runtime: 29 ms

class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        nums += nums
        res = [-1] * len(nums)
        stack = []
        for i, n in enumerate(nums[::-1]):
            while stack and n >= stack[-1]:
                stack.pop()
            
            if stack:
                res[len(nums)-i-1] = stack[-1]
            
            stack.append(n)
            
        return res[:len(nums)//2]
        