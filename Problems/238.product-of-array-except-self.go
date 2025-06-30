// title: Product of Array Except Self
// timestamp: 2024-04-18 15:18:35
// problemUrl: https://leetcode.com/problems/product-of-array-except-self/
// memory: 8 MB
// runtime: 32 ms

func productExceptSelf(nums []int) []int {
    leftProd, rightProd := make([]int, len(nums)), make([]int, len(nums))
    rightProd[0], leftProd[len(nums) - 1] = 1, 1
    for i := 1; i < len(nums) - 1; i++ {
        rightProd[i] = rightProd[i - 1] * nums[i - 1]
        leftProd[len(nums) - i - 1] = leftProd[len(nums) - i] * nums[len(nums) - i]
    }
    
    rightProd[len(nums) - 1] = rightProd[len(nums) - 2] * nums[len(nums) - 2]
    leftProd[0] = leftProd[1] * nums[1]

    for i := 0; i < len(leftProd); i++ {
        leftProd[i] *= rightProd[i]
    }

    return leftProd
}