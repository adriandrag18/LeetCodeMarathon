# title: Longest Common Prefix
# timestamp: 2025-06-08 23:49:20
# problemUrl: https://leetcode.com/problems/longest-common-prefix/
# memory: 17.8 MB
# runtime: 0 ms

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) < 1:
            return ''

        res = []
        i = 0
        while i < len(strs[0]):
            for s in strs[1:]:
                if i >= len(s) or s[i] != strs[0][i]:
                    break
            else:
                res.append(strs[0][i])
                i += 1
                continue
            break

        return strs[0][:i]