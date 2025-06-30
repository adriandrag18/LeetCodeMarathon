# title: Summary Ranges
# timestamp: 2025-06-12 12:17:07
# problemUrl: https://leetcode.com/problems/summary-ranges/
# memory: 18 MB
# runtime: 0 ms

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        ranges = []
        if len(nums) == 0:
            return []
        curr = (nums[0], nums[0])
        for num in nums[1:]:
            if curr[1] == num - 1:
                curr = (curr[0],num)
            else:
                ranges.append(curr)
                curr = (num, num)
        
        ranges.append(curr)

        return [f'{a}->{b}' if a != b else str(a) for a, b in ranges]