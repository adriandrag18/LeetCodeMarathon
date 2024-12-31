# title: Minimum Cost For Tickets
# timestamp: 2024-12-31 12:09:58
# problemUrl: https://leetcode.com/problems/minimum-cost-for-tickets/
# memory: 17.8 MB
# runtime: 1 ms

class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        daysArray = [0] * 366
        for day in days:
            daysArray[day] = 1
        
        dp = [0] * 366
        for i in range(1, 366):
            if not daysArray[i]:
                dp[i] = dp[i - 1]
                continue
            
            dp[i] = dp[i - 1] + costs[0]
            dp[i] = min(dp[i], dp[max(0, i - 7)] + costs[1])
            dp[i] = min(dp[i], dp[max(0, i - 30)] + costs[2])

        return dp[365]