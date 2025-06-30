# title: Palindrome Number
# timestamp: 2025-06-08 16:33:47
# problemUrl: https://leetcode.com/problems/palindrome-number/
# memory: 17.9 MB
# runtime: 1 ms

class Solution:
    def isPalindrome(self, x: int) -> bool:
        return str(x) == str(x)[::-1]