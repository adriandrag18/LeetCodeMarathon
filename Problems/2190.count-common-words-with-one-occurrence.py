# title: Count Common Words With One Occurrence
# timestamp: 2025-06-09 00:32:41
# problemUrl: https://leetcode.com/problems/count-common-words-with-one-occurrence/
# memory: 18.2 MB
# runtime: 0 ms

class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        counter1, counter2 = Counter(words1), Counter(words2)
        res = 0
        for word, count in counter1.items():
            if count == 1 and counter2.get(word, 0) == 1:
                res += 1
        
        return res