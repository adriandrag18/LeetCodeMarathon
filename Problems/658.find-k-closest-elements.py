# title: Find K Closest Elements
# timestamp: 2025-06-24 14:59:58
# problemUrl: https://leetcode.com/problems/find-k-closest-elements/
# memory: 18.9 MB
# runtime: 0 ms

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        n = len(arr)
        left = 0
        right = n - k
        while left < right:
            mid = (left + right) // 2
            if arr[mid + k] - x < x - arr[mid]:
                left = mid + 1
            else:
                right = mid
        
        return arr[left:left+k]
