# title: Max Difference You Can Get From Changing an Integer
# timestamp: 2025-06-15 14:41:35
# problemUrl: https://leetcode.com/problems/max-difference-you-can-get-from-changing-an-integer/
# memory: 17.5 MB
# runtime: 0 ms

class Solution:
    def maxDiff(self, num: int) -> int:
        s = str(num)
        i = 0
        while i < len(s) and s[i] == '9':
            i += 1
        if i == len(s):
            maxS = s
        else:
            maxS = s.replace(s[i], '9')
        
        minS = s.replace(s[0], '1')
        if s[0] != '1':
            return int(maxS) - int(minS)
        
        i = 0
        while i < len(s) and s[i] in '01':
            i += 1
        if i == len(s):
            minS = s
        else:
            minS = s.replace(s[i], '0')
        
        return int(maxS) - int(minS)