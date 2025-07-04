// title: Removing Stars From a String
// timestamp: 2024-04-17 09:29:23
// problemUrl: https://leetcode.com/problems/removing-stars-from-a-string/
// memory: 7.6 MB
// runtime: 32 ms

import (
    "strings"
)

func removeStars(s string) string {
    var stk []rune
    for _, c := range s {
        if c == '*' {
            stk = stk[:len(stk)-1]
            continue
        }
        stk =append(stk, c)
    }

    var builder strings.Builder
    for i := 0; i < len(stk); i++ {
        builder.WriteRune(stk[i])
    }

    return builder.String()
}