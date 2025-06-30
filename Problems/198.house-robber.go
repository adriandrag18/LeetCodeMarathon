// title: House Robber
// timestamp: 2024-04-17 20:58:04
// problemUrl: https://leetcode.com/problems/house-robber/
// memory: 2.3 MB
// runtime: 1 ms

func rob(nums []int) int {
    switch len(nums) {
    case 0:
        return 0
    case 1:
        return nums[0]
    case 2:
        if nums[0] < nums[1] {
            return nums[1]
        }
        return nums[0]
    }

    dp := make([]int, len(nums))
    dp[0], dp[1] = nums[0], nums[1]
    
    if nums[0] > nums[1] {
        dp[1] = nums[0]
    }

    for i := 2; i < len(nums); i++ {
        if dp[i-2] + nums[i] < dp[i-1] {
            dp[i] = dp[i-1]
            continue
        }
        dp[i] = dp[i-2] + nums[i]
    }
    
    return dp[len(dp)-1]
}