# title: Adding Spaces to a String
# timestamp: 2024-12-04 00:37:10
# problemUrl: https://leetcode.com/problems/adding-spaces-to-a-string/
# memory: 48.6 MB
# runtime: 118 ms

class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        m, n = len(spaces), len(s)
        t= [' '] * (m + n)
        j =  0
        for i, c in enumerate(s):
            if j < m and i == spaces[j]:
                j += 1
            t[i+j] = s[i]
        return "".join(t)       