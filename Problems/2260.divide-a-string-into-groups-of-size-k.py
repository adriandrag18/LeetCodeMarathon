# title: Divide a String Into Groups of Size k
# timestamp: 2025-06-22 11:22:21
# problemUrl: https://leetcode.com/problems/divide-a-string-into-groups-of-size-k/
# memory: 17.7 MB
# runtime: 0 ms

class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        res = []
        for i in range(0, len(s), k):
            res.append(s[i:i+k])
        
        if len(res[-1]) < k:
            res[-1] += fill * (k - len(res[-1]))
        
        return res