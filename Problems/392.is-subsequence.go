// title: Is Subsequence
// timestamp: 2024-04-15 17:00:20
// problemUrl: https://leetcode.com/problems/is-subsequence/
// memory: 2.3 MB
// runtime: 0 ms

func isSubsequence(s string, t string) bool {
    i := 0
    for j := 0; i < len(s) && j < len(t); j++ {
        if s[i] == t[j] {
            i++
        }
    }

    return i == len(s)
}