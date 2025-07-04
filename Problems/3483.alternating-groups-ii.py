# title: Alternating Groups II
# timestamp: 2025-03-09 21:46:50
# problemUrl: https://leetcode.com/problems/alternating-groups-ii/
# memory: 21.1 MB
# runtime: 759 ms

class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        n = len(colors)
        res = 0
        l, r = 0, 0
        while l < n:
            while colors[r % n] != colors[(r + 1) % n] and r < n + k - 1:
                r += 1
            if r == n + k - 1:
                r -= 1
            # print(l, r)
            if r - l + 1 >= k:
                res += r - l + 2 - k
            l, r = r + 1, r + 1
        
        return res

                