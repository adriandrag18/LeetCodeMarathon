# title: Shifting Letters
# timestamp: 2025-01-05 12:30:18
# problemUrl: https://leetcode.com/problems/shifting-letters/
# memory: 28.1 MB
# runtime: 102 ms

class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        for i in range(len(shifts) - 2, -1, -1):
            shifts[i] += shifts[i + 1]
        
        return ''.join([chr((ord(c) - ord('a') + shift) % 26 + ord('a')) for shift, c in zip(shifts, s)])