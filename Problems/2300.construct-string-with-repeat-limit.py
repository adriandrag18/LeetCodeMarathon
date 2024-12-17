# title: Construct String With Repeat Limit
# timestamp: 2024-12-17 03:56:05
# problemUrl: https://leetcode.com/problems/construct-string-with-repeat-limit/
# memory: 19.2 MB
# runtime: 204 ms

class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        alpha = [0] * 26
        for c, n in Counter(s).items():
            alpha[ord(c) - ord('a')] = n
        
        chars = []
        i = 25
        while i >= 0:
            if not alpha[i]:
                i -= 1
                continue
            
            c = chr(ord('a') + i)
            if repeatLimit >= alpha[i]:
                chars.extend([c] * alpha[i])
                alpha[i] = 0
                i -= 1
                continue
            
            alpha[i] -= repeatLimit
            chars.extend([c] * repeatLimit)

            for j in range(i - 1, -1, -1):
                if alpha[j]:
                    alpha[j] -= 1
                    chars.append(chr(ord('a') + j))
                    break
            else:
                break

        return ''.join(chars)