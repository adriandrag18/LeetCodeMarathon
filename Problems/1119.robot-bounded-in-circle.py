# title: Robot Bounded In Circle
# timestamp: 2025-06-12 21:58:49
# problemUrl: https://leetcode.com/problems/robot-bounded-in-circle/
# memory: 17.7 MB
# runtime: 0 ms

class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        pos = [0, 0]
        dir = 0
        dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        for ins in instructions:
            if ins == 'G':
                pos[0] += dirs[dir][0]
                pos[1] += dirs[dir][1]
            elif ins == 'L':
                dir = (dir + 3) % 4
            else:
                dir = (dir + 1) % 4
            # print(pos, dirs[dir])
        
        return pos == [0, 0] or dir != 0
