# title: Find the Number of Copy Arrays
# timestamp: 2025-03-01 16:48:02
# problemUrl: https://leetcode.com/problems/find-the-number-of-copy-arrays/
# memory: 68.8 MB
# runtime: 187 ms

class Solution:
    def countArrays(self, original: List[int], bounds: List[List[int]]) -> int:
        base = min(original)
        processed = [el - base for el in original]
        print(processed)
        bounds = [[bound[0] - el, bound[1] - el] for el, bound in zip(processed, bounds)]
        print(bounds)

        low, high = max([l for l, h in bounds]), min([h for l, h in bounds])
        print(low, high)
        
        return max(high - low + 1, 0)
        