# title: Container With Most Water
# timestamp: 2024-11-01 23:40:01
# problemUrl: https://leetcode.com/problems/container-with-most-water/
# memory: 27.6 MB
# runtime: 25 ms

class Solution:
    def maxArea(self, height: List[int]) -> int:
        i, j = 0, len(height) - 1
        res = min(height[i], height[j]) * (j - i)
        while i < j:
            if height[i] < height[j]:
                prev = height[i]
                i += 1
                while (height[i] < prev) and (i < j):
                    i += 1
            else:
                prev = height[j]
                j -= 1 
                while height[j] < prev and i < j:
                    j -= 1
            
            res = max(res, min(height[i], height[j]) * (j - i))

        return res