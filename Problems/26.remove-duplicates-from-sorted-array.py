# title: Remove Duplicates from Sorted Array
# timestamp: 2025-01-05 00:19:26
# problemUrl: https://leetcode.com/problems/remove-duplicates-from-sorted-array/
# memory: 18.9 MB
# runtime: 0 ms

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        freq = [False] * 201
        i = 0
        for num in nums:
            if freq[num + 100]:
                continue
            freq[num + 100] = True
            nums[i] = num
            i += 1

        return i

