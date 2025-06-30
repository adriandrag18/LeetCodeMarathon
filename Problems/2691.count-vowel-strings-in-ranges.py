# title: Count Vowel Strings in Ranges
# timestamp: 2025-01-02 03:29:19
# problemUrl: https://leetcode.com/problems/count-vowel-strings-in-ranges/
# memory: 50.2 MB
# runtime: 15 ms

class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        dp = [0] * (len(words) + 1)
        for i in range(len(words)):
            dp[i + 1] = dp[i] + (1 if words[i][0] in 'aeiou' and words[i][-1] in 'aeiou' else 0)
        
        return [dp[q[1] + 1] - dp[q[0]] for q in queries]