# title: Tuple with Same Product
# timestamp: 2025-06-01 21:17:28
# problemUrl: https://leetcode.com/problems/tuple-with-same-product/
# memory: 46.4 MB
# runtime: 367 ms

class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 4:
            return 0
        
        dp = defaultdict(int)

        count = 0
        for i in range(n):
            for j in range(i + 1, n):
                dp[nums[i] * nums[j]] += 1
            
        for key, cnt in dp.items():
            count += cnt * (cnt - 1) // 2

        return 8 * count