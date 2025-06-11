# title: Maximum Performance of a Team
# timestamp: 2025-01-06 13:21:55
# problemUrl: https://leetcode.com/problems/maximum-performance-of-a-team/
# memory: 35.1 MB
# runtime: 97 ms

class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        mod = 10**9 + 7
        arr = sorted(zip(efficiency, speed), reverse=True)
        heap, sum, res = [], 0, -1
        for num2, num1 in arr:
            heappush(heap, num1)
            sum += num1
            
            while len(heap) > k:
                sum -= heappop(heap)
            
            res = max(res, num2 * sum)
        
        return res % mod