# title: String Compression III
# timestamp: 2024-11-04 12:52:32
# problemUrl: https://leetcode.com/problems/string-compression-iii/
# memory: 28.3 MB
# runtime: 103 ms

class Solution:
    def compressedString(self, word: str) -> str:
        if len(word) == 0:
            return ''
        
        prev = word[0]
        num = 1
        res = []
        for c in word[1:]:
            if num < 9 and c == prev:
                num += 1
                continue
            res.append(str(num))
            res.append(prev)
            # print(res)
            prev = c
            num = 1
            
        res.append(str(num))
        res.append(prev)
        # print(res)

        return ''.join(res)
        