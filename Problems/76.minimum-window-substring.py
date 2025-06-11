# title: Minimum Window Substring
# timestamp: 2025-05-13 12:47:08
# problemUrl: https://leetcode.com/problems/minimum-window-substring/
# memory: 18.4 MB
# runtime: 55 ms

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ''

        res = (-1, 10**10)
        count, window = Counter(t), {}
        need, have = len(count), 0

        l = 0
        for r, c in enumerate(s):
            window[c] = window.get(c, 0) + 1
            if window[c] == count[c]:
                have += 1
            
            while have == need:
                if res[1] > r - l + 1:
                    res = (l, r - l + 1)

                c = s[l]
                window[c] -= 1
                if window[c] == count[c] - 1:
                    have -= 1
                
                l += 1

        return s[res[0]: res[0] + res[1]] if res[0] != -1 else ''