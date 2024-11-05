# title: Minimum Number of Changes to Make Binary String Beautiful
# timestamp: 2024-11-05 21:30:50
# problemUrl: https://leetcode.com/problems/minimum-number-of-changes-to-make-binary-string-beautiful/
# memory: 17 MB
# runtime: 26 ms

class Solution:
    def minChanges(self, s: str) -> int:
        # print(s)
        res = 0
        for i in range(int(len(s)/2)):
            # print(s[2*i:2*i+2])
            if s[2*i] != s[2*i+1]:
                res += 1
        return res