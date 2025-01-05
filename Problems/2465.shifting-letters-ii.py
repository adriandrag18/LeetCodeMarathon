# title: Shifting Letters II
# timestamp: 2025-01-05 12:40:12
# problemUrl: https://leetcode.com/problems/shifting-letters-ii/
# memory: 41.3 MB
# runtime: 53 ms

class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        freq = [0] * (len(s) + 1)
        for start, end, dir in shifts:
            shift = 1 if dir else -1
            freq[start] += shift
            freq[end + 1] += -shift

        for i in range(1, len(s)):
            freq[i] = freq[i - 1] + freq[i]
            
        return ''.join([chr((ord(c) - ord('a') + shift) % 26 + ord('a')) for shift, c in zip(freq, s)])        