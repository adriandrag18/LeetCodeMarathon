// title: Counting Bits
// timestamp: 2024-04-18 13:18:34
// problemUrl: https://leetcode.com/problems/counting-bits/
// memory: 4.7 MB
// runtime: 5 ms

func countBits(n int) []int {
    ans := make([]int, n + 1)
    ans[0] = 0

    for i := 1; i <= n; i++ {
        ans[i] = ans[i>>1] + (i & 1)
    }

    return ans
}