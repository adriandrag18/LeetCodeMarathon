// title: Min Cost Climbing Stairs
// timestamp: 2024-04-18 13:09:43
// problemUrl: https://leetcode.com/problems/min-cost-climbing-stairs/
// memory: 3.1 MB
// runtime: 2 ms

func minCostClimbingStairs(cost []int) int {
    dp := make([]int, len(cost))
    dp[0], dp[1] = cost[0], cost[1]

    for i := 2; i < len(cost); i++ {
        dp[i] = min(dp[i - 2], dp[i - 1]) + cost[i]
    }

    return min(dp[len(dp) - 2], dp[len(dp) - 1])
}