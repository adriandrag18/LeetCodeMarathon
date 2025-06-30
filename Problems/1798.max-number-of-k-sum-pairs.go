// title: Max Number of K-Sum Pairs
// timestamp: 2024-04-19 23:26:23
// problemUrl: https://leetcode.com/problems/max-number-of-k-sum-pairs/
// memory: 9.2 MB
// runtime: 98 ms

import (
    "sort"
    "fmt"
)
func maxOperations(nums []int, k int) int {
    sort.Ints(nums)

    var count int
    for i, j := 0, len(nums) - 1; i < j; {
        switch {
        case nums[i] + nums[j] == k:
            count++
            i++
            j--
        case nums[i] + nums[j] < k:
            i++
        case nums[i] + nums[j] > k: 
            j--
        }
    }

    return count
}