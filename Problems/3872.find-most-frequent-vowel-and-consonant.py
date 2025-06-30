# title: Find Most Frequent Vowel and Consonant
# timestamp: 2025-06-09 01:37:15
# problemUrl: https://leetcode.com/problems/find-most-frequent-vowel-and-consonant/
# memory: 17.8 MB
# runtime: 3 ms

class Solution:
    def maxFreqSum(self, s: str) -> int:
        counter = Counter(s)
        v = max([counter[c] for c in 'aeiou'] + [0])
        c = max([counter[c] for c in counter if c not in 'aeiou'] + [0])
        return v + c