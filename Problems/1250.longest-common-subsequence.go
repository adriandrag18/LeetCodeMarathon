// title: Longest Common Subsequence
// timestamp: 2024-04-23 15:49:21
// problemUrl: https://leetcode.com/problems/longest-common-subsequence/
// memory: 17.6 MB
// runtime: 12 ms

import "fmt"

func longestCommonSubsequence(text1 string, text2 string) int {
    dp := make([][]int, len(text1))
    for i := range text1 {
        dp[i] = make([]int, len(text2))
    }
    if text1[0] == text2[0] {
        dp[0][0] = 1
    }
    for i := 1; i < len(text1); i++ {
        if text1[i] == text2[0] || dp[i-1][0] == 1 {
            dp[i][0] = 1
        }
    }
    for i := 1; i < len(text2); i++ {
        if text2[i] == text1[0] || dp[0][i-1] == 1 {
            dp[0][i] = 1
        }
    }
    for i := 1; i < len(text1); i++ {
        for j := 1; j < len(text2); j++ {
            if text1[i] == text2[j] {
                dp[i][j] = dp[i-1][j-1] + 1
                continue
            }
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        }
    }
    return dp[len(text1)-1][len(text2)-1]
}