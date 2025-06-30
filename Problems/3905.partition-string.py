# title: Partition String 
# timestamp: 2025-06-29 05:37:27
# problemUrl: https://leetcode.com/problems/partition-string/
# memory: 25.6 MB
# runtime: 147 ms

class Solution:
    def partitionString(self, s: str) -> List[str]:
        segments = []
        curr = ''
        seen = set([''])
        for c in s:
            curr += c
            if curr not in seen:
                seen.add(curr)
                segments.append(curr)
                curr = ''

        # print(curr)
        return segments