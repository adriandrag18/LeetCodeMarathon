# title: Valid Palindrome
# timestamp: 2024-11-01 20:23:22
# problemUrl: https://leetcode.com/problems/valid-palindrome/
# memory: 16.7 MB
# runtime: 7 ms

class Solution:
    def isPalindrome(self, s: str) -> bool:
        i, j = 0, len(s) - 1
        while i < j:
            while i <= j and not s[i].isalnum():
                i += 1
            while i <= j and not s[j].isalnum():
                j -= 1
            if i <= j and s[i].lower() != s[j].lower():
                return False
            i += 1
            j -= 1
        return True
