# title: Flip Columns For Maximum Number of Equal Rows
# timestamp: 2024-11-23 00:56:37
# problemUrl: https://leetcode.com/problems/flip-columns-for-maximum-number-of-equal-rows/
# memory: 20 MB
# runtime: 23 ms

class Solution:
    def maxEqualRowsAfterFlips(self, mat: List[List[int]]) -> int:
        pat_freq = Counter()
        
        for r in mat:
            pattern = tuple(r) if r[0] == 0 else tuple(bit ^ 1 for bit in r)
            pat_freq[pattern] += 1
            
        return max(pat_freq.values())