// title: Maximum Average Subarray I
// timestamp: 2024-04-18 12:33:59
// problemUrl: https://leetcode.com/problems/maximum-average-subarray-i/
// memory: 10.7 MB
// runtime: 119 ms

func findMaxAverage(nums []int, k int) float64 {
    var window int
    for i := 0; i < k; i++ {
        window += nums[i]
    }
    
    max := float64(window) / float64(k)

    for i := k; i < len(nums); i++ {
        window += nums[i] - nums[i - k]
        avg := float64(window) / float64(k)
        if max < avg {
            max = avg
        }
    }

    return max
}