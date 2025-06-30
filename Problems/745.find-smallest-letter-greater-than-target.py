# title: Find Smallest Letter Greater Than Target
# timestamp: 2025-06-10 20:21:18
# problemUrl: https://leetcode.com/problems/find-smallest-letter-greater-than-target/
# memory: 19.1 MB
# runtime: 0 ms

class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        target = ord(target) - ord('a')
        for i in range(target + 1, 26):
            letter = chr(i + 97)
            if letter in letters:
                return letter
            
        return letters[0]