# title: Construct K Palindrome Strings
# timestamp: 2025-01-11 02:53:30
# problemUrl: https://leetcode.com/problems/construct-k-palindrome-strings/
# memory: 18.2 MB
# runtime: 28 ms

class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        if k > len(s):
            return False
        if k == len(s):
            return True

        return k >= sum([count % 2 for count in Counter(s).values()])