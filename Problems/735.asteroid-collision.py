# title: Asteroid Collision
# timestamp: 2025-06-18 00:11:47
# problemUrl: https://leetcode.com/problems/asteroid-collision/
# memory: 19 MB
# runtime: 3 ms

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        res = []
        for asteroid in asteroids:
            if asteroid < 0:
                eq = False
                while len(res) != 0:
                    if res[-1] < 0:
                        res.append(asteroid)
                        break
                    if res[-1] < -asteroid:
                        res.pop()
                        continue
                    if res[-1] == -asteroid:
                        res.pop()
                        eq = True
                        break
                    break
                if len(res) == 0 and not eq:
                    res.append(asteroid)
                continue
            
            res.append(asteroid)
        
        return res