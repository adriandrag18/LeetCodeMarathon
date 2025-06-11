# title: Maximum Difference Between Even and Odd Frequency II
# timestamp: 2025-06-11 19:15:44
# problemUrl: https://leetcode.com/problems/maximum-difference-between-even-and-odd-frequency-ii/
# memory: 20.9 MB
# runtime: 2114 ms

class Solution:
    def maxDifference(self, s: str, k: int) -> int:
        n = len(s)
        chars = '01234'
        map = {c: [0] for c in chars}
        for i in range(1, n+1):
            map[s[i-1]].append(map[s[i-1]][i-1] + 1)
            for c in [c for c in chars if c != s[i-1]]:
                map[c].append(map[c][i-1])
                
        res = -float('inf')
        for a in chars:
            for  b in chars:
                if a == b: 
                    continue
                fa, fb = map[a], map[b]
                bests = [[-float('inf'), -float('inf')], [-float('inf'), -float('inf')]]
                l = 0
                for r in range(k, n + 1):
                    while r - l >= k and fa[r] - fa[l] > 0 and fb[r] - fb[l] > 0:
                        pa, pb = fa[l] % 2, fb[l] % 2
                        bests[pa][pb] = max(bests[pa][pb], fb[l] - fa[l])
                        l += 1
                        
                    pa, pb = fa[r] % 2, fb[r] % 2

                    if bests[1 - pa][pb] != -float('inf'):
                        res = max(res, bests[1 - pa][pb] + fa[r] - fb[r])
                    
        
        return res