# title: Check If It Is a Straight Line
# timestamp: 2025-06-12 21:12:37
# problemUrl: https://leetcode.com/problems/check-if-it-is-a-straight-line/
# memory: 18.2 MB
# runtime: 0 ms

class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        p1, p2 = coordinates[0], coordinates[1]
        if p1[0] > p2[0]:
            p1, p2 = p2, p1
        prev = (p1[1] - p2[1]) / (p1[0] - p2[0]) if p1[0] - p2[0] != 0 else float('inf')
        for i in range(1, len(coordinates) - 1):
            p1, p2 = coordinates[i], coordinates[i + 1]
            if p1[0] > p2[0]:
                p1, p2 = p2, p1
            m = (p1[1] - p2[1]) / (p1[0] - p2[0]) if p1[0] - p2[0] != 0 else float('inf')
            if not (m == float('inf') and prev == float('inf')) and abs(m - prev) > 0.000001:
                return False
        
        return True