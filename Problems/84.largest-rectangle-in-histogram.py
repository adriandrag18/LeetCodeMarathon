# title: Largest Rectangle in Histogram
# timestamp: 2024-11-11 22:08:53
# problemUrl: https://leetcode.com/problems/largest-rectangle-in-histogram/
# memory: 34.4 MB
# runtime: 172 ms

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        res = 0
        stack = []
        for i, h in enumerate(heights):
            n = i
            while stack and stack[-1][1] > h:
                j, hi = stack.pop()
                res = max(res, (i - j) * hi)
                # print(f'i={i}, h={h}, j={j}, hi={hi} max={res}')
                n = min(n, j)
            stack.append((n, h))
        
        while stack:
            j, hi = stack.pop()
            res = max(res, (len(heights) - j) * hi)

        return res
