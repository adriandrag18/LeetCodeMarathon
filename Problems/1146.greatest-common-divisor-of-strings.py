# title: Greatest Common Divisor of Strings
# timestamp: 2024-12-27 00:45:57
# problemUrl: https://leetcode.com/problems/greatest-common-divisor-of-strings/
# memory: 17.9 MB
# runtime: 0 ms

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1 + str2 != str2 + str1:
            return ''
        
        def gcd(n, m):
            if n < m:
                n, m = m, n
            while m:
                n, m = m, n % m
            return n

        return str2[:gcd(len(str1), len(str2))]