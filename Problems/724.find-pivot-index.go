// title: Find Pivot Index
// timestamp: 2024-04-18 12:41:35
// problemUrl: https://leetcode.com/problems/find-pivot-index/
// memory: 6.4 MB
// runtime: 13 ms

func pivotIndex(nums []int) int {
    var sum int
    for _, num := range nums {
        sum += num
    }

    var leftSum, rightSum int
    for i, num := range nums {
        rightSum = sum - num - leftSum
        if leftSum == rightSum {
            return i
        }
        leftSum += num
    }
    
    return -1
}