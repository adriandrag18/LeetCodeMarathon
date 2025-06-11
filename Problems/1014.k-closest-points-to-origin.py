# title: K Closest Points to Origin
# timestamp: 2025-01-02 18:39:45
# problemUrl: https://leetcode.com/problems/k-closest-points-to-origin/
# memory: 23 MB
# runtime: 47 ms

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dist = [(sqrt(p[0] * p[0] + p[1] * p[1]), p) for p in points]
        return [x[1] for x in sorted(dist)[:k]]