# title: Robot Return to Origin
# timestamp: 2025-06-12 22:07:36
# problemUrl: https://leetcode.com/problems/robot-return-to-origin/
# memory: 17.9 MB
# runtime: 15 ms

class Solution:
    def judgeCircle(self, moves: str) -> bool:
        x, y = 0, 0
        for m in moves:
            if m == 'U':
                x += 1
            elif m == 'D':
                x -= 1
            elif m == 'R':
                y += 1
            else:
                y -= 1
        return x == 0 and y == 0