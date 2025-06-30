# title: Largest Combination With Bitwise AND Greater Than Zero
# timestamp: 2024-11-07 14:17:44
# problemUrl: https://leetcode.com/problems/largest-combination-with-bitwise-and-greater-than-zero/
# memory: 26.7 MB
# runtime: 503 ms

class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        if len(candidates) < 2:
            return len(candidates)
        
        count = [0 for _ in range(32)]
        for c in candidates:
            n = 0
            while c:
                if c & 1:
                    count[n] += 1
                n += 1
                c = c >> 1
                
        return max(count)
