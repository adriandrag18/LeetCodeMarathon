// title: Best Time to Buy and Sell Stock with Transaction Fee
// timestamp: 2024-04-23 16:31:56
// problemUrl: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/
// memory: 7.4 MB
// runtime: 52 ms

func maxProfit(prices []int, fee int) int {
    if len(prices) == 0 || len(prices) == 1 {
        return 0
    }

    dp := make([][]int, 2)
    dp[0] = make([]int, len(prices))
    dp[1] = make([]int, len(prices))
    dp[0][0] = 0
    dp[1][0] = -prices[0]

    for i := 1; i < len(prices); i++ {
        dp[0][i] = max(dp[0][i-1], dp[1][i-1] + prices[i] - fee)
        dp[1][i] = max(dp[1][i-1], dp[0][i-1] - prices[i])
    }

    return dp[0][len(prices)-1]
}