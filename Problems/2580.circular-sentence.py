# title: Circular Sentence
# timestamp: 2024-11-03 12:34:14
# problemUrl: https://leetcode.com/problems/circular-sentence/
# memory: 16.6 MB
# runtime: 0 ms

class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        words = sentence.split(' ')
        
        for i in range(len(words)):
            if words[i][0] != words[i-1][-1]:
                return False
        
        return True