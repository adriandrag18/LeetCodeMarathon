# title: String Compression
# timestamp: 2024-11-04 12:47:00
# problemUrl: https://leetcode.com/problems/string-compression/
# memory: 17 MB
# runtime: 65 ms

class Solution:
    def compress(self, chars: List[str]) -> int:
        if len(chars) < 2:
            return len(chars)
        
        prev = chars[0]
        num = 1
        res = []
        for c in chars[1:]:
            if c == prev:
                num += 1
                continue
            res.append(prev)
            if num > 1:
                res.append(str(num))
            print(res)
            prev = c
            num = 1
            
        res.append(prev)
        if num > 1:
            res.append(str(num))
        print(res)
        res = ''.join(res)

        chars.clear()
        chars.extend([c for c in res])
        print(chars)
        return len(res)