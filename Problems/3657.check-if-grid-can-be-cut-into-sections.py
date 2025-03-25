# title: Check if Grid can be Cut into Sections
# timestamp: 2025-03-25 11:00:13
# problemUrl: https://leetcode.com/problems/check-if-grid-can-be-cut-into-sections/
# memory: 83.6 MB
# runtime: 483 ms

class Solution:
    def checkValidCuts(self, n: int, rectangles: List[List[int]]) -> bool:
        for k in range(2):
            if k == 1:
                rectangles = [[r[1], r[0], r[3], r[2]] for r in rectangles]
            
            rectangles.sort()
            new = []
            a, b = rectangles[0][0], rectangles[0][2]
            for r in rectangles[1:]:
                if r[0] < b:
                    b = max(b, r[2])
                    continue
                new.append((a, b))
                if len(new) >= 2:
                    return True
                a, b = r[0], r[2]
        
        return False