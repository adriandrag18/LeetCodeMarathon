// title: Reverse Words in a String
// timestamp: 2024-04-15 16:41:44
// problemUrl: https://leetcode.com/problems/reverse-words-in-a-string/
// memory: 3.9 MB
// runtime: 2 ms

import (
    "strings"
)

func reverseWords(s string) string {
    parts := strings.Split(s, " ")
    parts = reverseSlice(parts)
    return strings.Join(parts,  " ")
}
func reverseSlice(slice []string) []string {
    reversed := make([]string, 0)
    for i := 0; i < len(slice); i++ {
        if slice[len(slice)-1-i] == "" {
            continue
        }
        reversed = append(reversed, slice[len(slice)-1-i])
    }
    return reversed
}