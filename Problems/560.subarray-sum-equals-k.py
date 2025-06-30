# title: Subarray Sum Equals K
# timestamp: 2025-06-06 16:04:04
# problemUrl: https://leetcode.com/problems/subarray-sum-equals-k/
# memory: 21.9 MB
# runtime: 43 ms

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count, n = 0, len(nums)
        prev = 0
        map = defaultdict(int)
        map[k] = 1
        for i in range(1, n + 1):
            prefix = prev + nums[i - 1]
            prev = prefix
            count += map[prefix]
            map[k + prefix] += 1
        
        return count