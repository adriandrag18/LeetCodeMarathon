# title: Find Maximum Area of a Triangle
# timestamp: 2025-06-21 19:34:04
# problemUrl: https://leetcode.com/problems/find-maximum-area-of-a-triangle/
# memory: 61.6 MB
# runtime: 383 ms

class Solution:
    def maxArea(self, coords: List[List[int]]) -> int:
        map = defaultdict(list)
        for x, y in coords:
            map[x].append(y)
        
        res = -1
        xs = sorted(map.keys())
        for x, li in map.items():
            if len(li) < 2:
                continue

            l = max(li) - min(li)
            for x2 in [xs[0], xs[-1]]:
                if x2 == x:
                    continue
                h = abs(x2 - x)
                res = max(res, l * h)

        
        map = defaultdict(list)
        for x, y in coords:
            map[y].append(x)

        ys = sorted(map.keys())
        for y, li in map.items():
            if len(li) < 2:
                continue

            l = max(li) - min(li)
            for y2 in [ys[0], ys[-1]]:
                if y2 == y:
                    continue
                h = abs(y2 - y)
                res = max(res, l * h)

        return res
            