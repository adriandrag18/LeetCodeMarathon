// title: Longest Ideal Subsequence
// timestamp: 2024-04-26 15:37:52
// problemUrl: https://leetcode.com/problems/longest-ideal-subsequence/
// memory: 5.2 MB
// runtime: 22 ms

import "fmt"

func longestIdealString(s string, k int) int {
    switch len(s) {
    case 0: 
        return 0
    case 1:
        return 1
    }
    
    dp := make([]int, 26)
    for _, c := range s {
        i, k, curr := c - 'a', rune(k), 1
        for j := max(0, i - k); j < min(26, i + k + 1); j++ {
            curr = max(curr, dp[j] + 1)
        }
        dp[i] = curr
        // fmt.Println(dp)
    }

    var max int
    for _, no := range dp {
        if max < no {
            max = no
        }
    }
    return max
}
