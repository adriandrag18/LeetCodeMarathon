# title: Delete Characters to Make Fancy String
# timestamp: 2024-11-01 21:06:27
# problemUrl: https://leetcode.com/problems/delete-characters-to-make-fancy-string/
# memory: 18.7 MB
# runtime: 379 ms

class Solution:
    def makeFancyString(self, s: str) -> str:
        if len(s) < 3:
            return s
        chars = [s[0], s[1]]
        for c in s[2:len(s)]:
            if chars[len(chars) - 2] == chars[len(chars) - 1] == c:
                continue
            chars.append(c)
        
        return ''.join(chars)
        