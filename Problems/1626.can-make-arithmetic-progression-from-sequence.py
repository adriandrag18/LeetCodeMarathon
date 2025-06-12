# title: Can Make Arithmetic Progression From Sequence
# timestamp: 2025-06-12 20:34:11
# problemUrl: https://leetcode.com/problems/can-make-arithmetic-progression-from-sequence/
# memory: 18 MB
# runtime: 0 ms

class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()
        return all([arr[i+2] - arr[i+1] == arr[i+1] - arr[i] for i in range(len(arr) - 2)])