# title: Find the Prefix Common Array of Two Arrays
# timestamp: 2025-01-15 00:46:59
# problemUrl: https://leetcode.com/problems/find-the-prefix-common-array-of-two-arrays/
# memory: 17.8 MB
# runtime: 11 ms

class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        seenA, seenB = set(), set()
        count = 0
        res = []
        for a, b in zip(A, B):
            if a in seenB:
                seenB.remove(a)
                count += 1
            else:
                seenA.add(a)
            if b in seenA:
                seenA.remove(b)
                count += 1
            else:
                seenB.add(b)
            
            res.append(count)
        
        return res
