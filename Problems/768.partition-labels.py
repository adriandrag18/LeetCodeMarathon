# title: Partition Labels
# timestamp: 2025-06-04 17:37:21
# problemUrl: https://leetcode.com/problems/partition-labels/
# memory: 17.9 MB
# runtime: 2 ms

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastIndexOf = {}
        for i, c in enumerate(s):
            lastIndexOf[c] = i
            
        partitions = []
        start, end = 0, 0
        for i, c in enumerate(s):
            end = max(end, lastIndexOf[s[i]])
            if i < end:
                continue
            partitions.append(end - start + 1)
            start, end = i + 1, i + 1

        return partitions