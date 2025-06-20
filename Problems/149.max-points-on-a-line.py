# title: Max Points on a Line
# timestamp: 2025-06-20 23:49:22
# problemUrl: https://leetcode.com/problems/max-points-on-a-line/
# memory: 39.6 MB
# runtime: 55 ms

class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        if len(points) < 2:
            return len(points)

        points.sort()
        map = defaultdict(set)
        for i, (x, y) in enumerate(points):
            for j in range(i + 1, len(points)):
                x2, y2 = points[j]
                if x2 != x:
                    m = (y2 - y) / (x2 - x)
                    axesInt = (0, y - m * x)
                else:
                    m = float('inf')
                    axesInt = (x, 0)
                map[(m, axesInt)].add(i)
                map[(m, axesInt)].add(j)
        
        return max([len(s) for s in map.values()])