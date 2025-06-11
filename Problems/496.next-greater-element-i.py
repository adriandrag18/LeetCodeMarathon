# title: Next Greater Element I
# timestamp: 2025-05-13 15:32:35
# problemUrl: https://leetcode.com/problems/next-greater-element-i/
# memory: 18.1 MB
# runtime: 0 ms

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n1, n2 = len(nums1), len(nums2)
        stack = []
        nextBig = [-1] * n2
        for i in range(n2-1, -1, -1):
            while stack and nums2[i] >= stack[-1]:
                stack.pop()
                # print(stack)
            if stack:
                nextBig[i] = stack[-1]
            stack.append(nums2[i])
            # print(stack)
        
        indexOf = {}
        for i, n in enumerate(nums2):
            indexOf[n] = i
        
        res = []
        for n in nums1:
            if n not in indexOf:
                res.append(-1)
                continue
            res.append(nextBig[indexOf[n]])
        
        return res