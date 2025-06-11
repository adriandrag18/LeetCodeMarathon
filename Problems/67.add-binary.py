# title: Add Binary
# timestamp: 2025-06-09 14:14:56
# problemUrl: https://leetcode.com/problems/add-binary/
# memory: 17.6 MB
# runtime: 0 ms

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return bin(int(a, 2) + int(b, 2))[2:]