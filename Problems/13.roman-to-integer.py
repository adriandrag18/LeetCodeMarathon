# title: Roman to Integer
# timestamp: 2025-01-07 21:16:32
# problemUrl: https://leetcode.com/problems/roman-to-integer/
# memory: 17.8 MB
# runtime: 4 ms

class Solution:
    def romanToInt(self, s: str) -> int:
        map = {
            'M': 1000, 
            'CM': 900,
            'D': 500,
            'CD': 400,
            'C': 100,
            'XC': 90,
            'L': 50,
            'XL': 40,
            'X': 10,
            'IX': 9,
            'V': 5,
            'IV': 4,
            'I': 1,
        }
        i = 0
        num = 0
        while i < len(s) - 1:
            # print(num)
            if s[i:i+2] in map:
                num += map[s[i:i+2]]
                i += 2
                continue
            num += map[s[i]]
            i += 1
        # print(num)
        if i == len(s) - 1:
            num += map[s[i]]
            # print(num)
        
        return num
