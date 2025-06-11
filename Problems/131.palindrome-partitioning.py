# title: Palindrome Partitioning
# timestamp: 2025-01-10 08:59:24
# problemUrl: https://leetcode.com/problems/palindrome-partitioning/
# memory: 34.5 MB
# runtime: 56 ms

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def isPalindrom(s):
            return s == s[::-1]
        
        def helper(i, l):
            if i == len(s):
                res.append(l[:])
                return 
            
            for j in range(i + 1, len(s) + 1):
                # print(s[i:j], isPalindrom(s[i:j]))
                if isPalindrom(s[i:j]):
                    l.append(s[i:j])
                    helper(j, l)
                    l.pop()
        
        res = []
        helper(0, [])
        return res