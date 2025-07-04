# title: Optimal Partition of String
# timestamp: 2025-07-04 12:55:58
# problemUrl: https://leetcode.com/problems/optimal-partition-of-string/
# memory: 17.9 MB
# runtime: 55 ms

class Solution:
    def partitionString(self, s: str) -> int:
        count = 1
        seen = set()
        for c in s:
            if c in seen:
                count += 1
                seen = set([c])
            else:
                seen.add(c)

        return count
