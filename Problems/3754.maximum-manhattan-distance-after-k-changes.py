# title: Maximum Manhattan Distance After K Changes
# timestamp: 2025-06-20 21:10:00
# problemUrl: https://leetcode.com/problems/maximum-manhattan-distance-after-k-changes/
# memory: 18.1 MB
# runtime: 3155 ms

class Solution:
    def maxDistance(self, s: str, k: int) -> int:
        map = {
            'N': (0, 1),
            'S': (0, -1),
            'E': (1, 0),
            'W': (-1, 0),
        }
        counter = Counter(s)
        pos = (0, 0)
        maxTotal = 0
        curr = {'N': 0, 'S': 0, 'E': 0, 'W': 0}
        for c in s:
            curr[c] += 1
            dx, dy = map[c]
            pos = (pos[0] + dx, pos[1] + dy)
            dist = abs(pos[0]) + abs(pos[1])
            
            if pos[0] < 0:
                antiX = 'E'
            else:
                antiX = 'W'    
            
            if pos[1] < 0:
                antiY = 'N'
            else:
                antiY = 'S'
            
            # print(pos, dist, antiX, antiY)

            countAnti = curr[antiX] + curr[antiY]
            currTotal = dist + 2 * min(k, countAnti)
            remaining = k - countAnti
            # print(currTotal, countAnti)
            if remaining > 0:
                countAnti = counter[antiX] + counter[antiY] - countAnti
                currTotal += min(remaining, countAnti)
            # print(currTotal)
            maxTotal = max(maxTotal, currTotal)

        return maxTotal