// title: Single Number
// timestamp: 2024-04-18 13:22:00
// problemUrl: https://leetcode.com/problems/single-number/
// memory: 6.3 MB
// runtime: 13 ms

func singleNumber(nums []int) int {
    var res int
    for _, num := range nums {
        res ^= num
    }
    return res
}