// title: Determine if Two Strings Are Close
// timestamp: 2024-04-14 22:50:25
// problemUrl: https://leetcode.com/problems/determine-if-two-strings-are-close/
// memory: 6.6 MB
// runtime: 56 ms

import (
    "reflect"
    "sort"
    "fmt"
)

func closeStrings(word1 string, word2 string) bool {
    if len(word1) != len(word2) {
        return false
    }
    
    word1letters, word2letters := make(map[rune]int), make(map[rune]int)
    for _, c := range word1 {
        // if _, ok := word1letters[c]; !ok {
        //     word1letters[c] = 0
        // }
        word1letters[c] += 1
    }    
    
    for _, c := range word2 {
        // if _, ok := word2letters[c]; !ok {
        //     word2letters[c] = 0
        // }
        word2letters[c] += 1
    }


    word1num, word2num := make([]int, 0), make([]int, 0)
    word1let, word2let := make(map[rune]bool), make(map[rune]bool)

    for c, num := range word1letters {
        word1let[c] = true
        word1num = append(word1num, num)
    }
    for c, num := range word2letters {
        word2let[c] = true
        word2num = append(word2num, num)
    }

    sort.Sort(sort.IntSlice(word1num))
    sort.Sort(sort.IntSlice(word2num))

    return reflect.DeepEqual(word1let, word2let) && reflect.DeepEqual(word1num, word2num)
}