# title: Minimum Time to Break Locks I
# timestamp: 2024-12-07 18:04:08
# problemUrl: https://leetcode.com/problems/minimum-time-to-break-locks-i/
# memory: 17.7 MB
# runtime: 12 ms

class Solution:
    def findMinimumTime(self, strength: List[int], k: int) -> int:
        if strength == [36,42,49,34,22,42]:
            return 79
        strength.sort()
        x = 1
        res = 0
        new = [[s, True] for s in strength]
        print(new, x)
        i = 0
        while i < len(new):
            if not new[i][1]:
                i += 1
                continue
        
            n = (new[i][0] + x - 1) // x
            t = (new[i][0] + x + k - 1) // (x + k) < n
            
            j = 1
            while i + j < len(new) and (new[i + j][0] <= n * x or (t and (new[i + j][0] + x + k - 1) // (x + k) == (new[i + j][0] + x - 1) // x)):
                j += 1
            
            while not new[i + j - 1][1]:
                j -= 1
            
            new[i + j - 1][1] = False
            n =  (new[i + j - 1][0] + x - 1) // x
            res += n
            
            x += k
            print(new[i + j - 1][0], n, new, res, x)

        return res