# title: Make String a Subsequence Using Cyclic Increments
# timestamp: 2024-12-04 11:31:31
# problemUrl: https://leetcode.com/problems/make-string-a-subsequence-using-cyclic-increments/
# memory: 17.5 MB
# runtime: 64 ms

class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        if len(str1) < len(str2):
            return False
        map = {'z': 'a'}
        for i in range(25):
            map[chr(ord('a') + i)] = chr(ord('a') + i + 1)
        i = 0
        for c in str1:
            # print(c, str2[i], map[str2[i]], not (c == str2[i] or c == map[str1[i]]))
            if str2[i] not in [c, map[c]]:
                continue
            i += 1
            if i == len(str2):
                break
        return i == len(str2)