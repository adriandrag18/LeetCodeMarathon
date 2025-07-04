# title: Eliminate Maximum Number of Monsters
# timestamp: 2025-06-09 00:41:39
# problemUrl: https://leetcode.com/problems/eliminate-maximum-number-of-monsters/
# memory: 32.2 MB
# runtime: 67 ms

class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        times = sorted([d/s for d, s in zip(dist, speed)])
        count = 0
        while count < len(times) and count < times[count]:
            count += 1
        
        return count