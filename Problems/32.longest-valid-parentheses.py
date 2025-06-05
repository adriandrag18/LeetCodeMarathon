# title: Longest Valid Parentheses
# timestamp: 2025-06-05 12:36:39
# problemUrl: https://leetcode.com/problems/longest-valid-parentheses/
# memory: 18.1 MB
# runtime: 7 ms

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        curr = count = res = 0
        for c in s:
            curr += 1 if c == '(' else -1
            count += 1
            if curr < 0:
                curr = count = 0
            elif curr == 0:
                res = max(res, count)
        
        curr = count = 0
        for c in s[::-1]:
            curr += 1 if c == ')' else -1
            count += 1
            # print(c, curr, count)
            if curr < 0:
                curr = count = 0
            elif curr == 0:
                res = max(res, count)
            # print('\t', res)
        
        return res
