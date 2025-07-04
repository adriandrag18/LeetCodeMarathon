# title: Continuous Subarrays
# timestamp: 2024-12-14 23:58:36
# problemUrl: https://leetcode.com/problems/continuous-subarrays/
# memory: 28 MB
# runtime: 1048 ms

from sortedcontainers import SortedList

class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        sorted_window = SortedList()  # To maintain the current window's sorted elements
        start = 0
        total_subarrays = 0
        
        for end in range(n):
            # Add the current element to the sorted window
            sorted_window.add(nums[end])
            
            # Ensure the window is valid
            while sorted_window[-1] - sorted_window[0] > 2:
                # Remove the leftmost element from the window
                sorted_window.remove(nums[start])
                start += 1
            
            # Count valid subarrays ending at 'end'
            total_subarrays += end - start + 1
        
        return total_subarrays