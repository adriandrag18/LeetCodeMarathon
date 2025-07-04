# title: Daily Temperatures
# timestamp: 2024-11-08 05:21:08
# problemUrl: https://leetcode.com/problems/daily-temperatures/
# memory: 26 MB
# runtime: 111 ms

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack, next = [], [0 for _ in temperatures]
        for i in range(len(temperatures) - 1, -1, -1):
            while stack and temperatures[stack[-1]] <= temperatures[i]: 
                stack.pop()
            if stack:
                next[i] = stack[-1] - i
            stack.append(i)
        
        return next
