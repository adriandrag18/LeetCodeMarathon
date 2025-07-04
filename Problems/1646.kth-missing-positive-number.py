# title: Kth Missing Positive Number
# timestamp: 2025-06-12 12:28:53
# problemUrl: https://leetcode.com/problems/kth-missing-positive-number/
# memory: 17.5 MB
# runtime: 0 ms

class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        l, r = 0, len(arr) - 1
        while l <= r:
            mid = (l + r) // 2
            missing = arr[mid] - mid - 1
            if missing < k:
                l = mid + 1
            else:
                r = mid - 1
        
        return l + k