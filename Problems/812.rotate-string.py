# title: Rotate String
# timestamp: 2024-11-03 12:28:38
# problemUrl: https://leetcode.com/problems/rotate-string/
# memory: 16.7 MB
# runtime: 0 ms

class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False

        for i in range(len(s)):
            found = True
            for j in range(len(s)):
                if goal[j] != s[(i + j) % len(s)]:
                    found = False
                    break
            if found:
                return True
        
        return False