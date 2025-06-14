# title: Maximum Difference by Remapping a Digit
# timestamp: 2025-06-14 11:28:23
# problemUrl: https://leetcode.com/problems/maximum-difference-by-remapping-a-digit/
# memory: 17.8 MB
# runtime: 0 ms

class Solution:
    def minMaxDifference(self, num: int) -> int:
        s = str(num)
        i = 0
        while i < len(s) and s[i] == '9':
            i += 1
        if i == len(s):
            maxS = s
        else:
            maxS = s.replace(s[i], '9')
        minS = s.replace(s[0], '0')

        return int(maxS) - int(minS)