# title: Find the Lexicographically Largest String From the Box I
# timestamp: 2025-06-04 16:57:06
# problemUrl: https://leetcode.com/problems/find-the-lexicographically-largest-string-from-the-box-i/
# memory: 17.9 MB
# runtime: 7 ms

class Solution:
    def answerString(self, word: str, numFriends: int) -> str:
        if numFriends == 1:
            return word
        n, m = len(word), len(word) - numFriends + 1
        char = max(word)
        res = ''
        for i in range(n):
            if word[i] == char:
                res = max(res, word[i:i+m])
        
        return res