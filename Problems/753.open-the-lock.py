# title: Open the Lock
# timestamp: 2025-06-18 00:19:31
# problemUrl: https://leetcode.com/problems/open-the-lock/
# memory: 18.1 MB
# runtime: 15 ms

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        pow10 = [1, 10, 100, 1000]
        visit = [0] * 10000  # 0: not visited, 1: visited forward, -1: visited backward, 2: deadends
        for dead in deadends:
            num = int(dead)
            visit[num] = 2
        
        src = 0
        dest = int(target)
        steps = 0
        dir = 1
        
        if visit[src] == 2 or visit[dest] == 2:
            return -1
        if src == dest:
            return 0
        
        forward = [src]
        backward = [dest]
        visit[src] = 1
        visit[dest] = -1
        
        while forward and backward:
            if len(forward) > len(backward):
                forward, backward = backward, forward
                dir = -dir
            
            steps += 1
            size = len(forward)
            for _ in range(size):
                cur = forward.pop(0)
                for p in pow10:
                    d = (cur // p) % 10
                    for i in [-1, 1]:
                        z = d + i
                        if z == -1:
                            z = 9
                        elif z == 10:
                            z = 0
                        next_state = cur + (z - d) * p
                        if visit[next_state] == -dir:
                            return steps
                        if visit[next_state] == 0:
                            forward.append(next_state)
                            visit[next_state] = dir
        
        return -1