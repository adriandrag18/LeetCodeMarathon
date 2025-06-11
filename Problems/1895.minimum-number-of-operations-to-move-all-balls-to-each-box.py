# title: Minimum Number of Operations to Move All Balls to Each Box
# timestamp: 2025-01-06 03:30:30
# problemUrl: https://leetcode.com/problems/minimum-number-of-operations-to-move-all-balls-to-each-box/
# memory: 17.9 MB
# runtime: 9 ms

class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n = len(boxes)
        left, right = [0] * n, [0] * n
        count = 0
        for i in range(1, n):
            count += 1 if boxes[i - 1] == '1' else 0
            left[i] = left[i - 1] + count
        
        count = 0
        for i in range(n - 2, -1, -1):
            count += 1 if boxes[i + 1] == '1' else 0
            right[i] = right[i + 1] + count
        
        for i in range(n):
            right[i] += left[i]

        return right
