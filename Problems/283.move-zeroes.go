// title: Move Zeroes
// timestamp: 2024-04-15 16:50:27
// problemUrl: https://leetcode.com/problems/move-zeroes/
// memory: 7.1 MB
// runtime: 15 ms

func moveZeroes(nums []int)  {
    i := 0
    for j := 0; j < len(nums); j++ {
        if nums[j] == 0{
            continue
        }
        nums[i] = nums[j]
        i++
    }

    for ; i < len(nums); i++ {
        nums[i] = 0
    }
}