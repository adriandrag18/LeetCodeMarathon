// title: Trapping Rain Water
// timestamp: 2024-04-14 21:02:05
// problemUrl: https://leetcode.com/problems/trapping-rain-water/
// memory: 6.2 MB
// runtime: 8 ms

func trap(heights []int) int {
    lenght := len(heights)
    maxLeft, maxRight := make([]int, lenght), make([]int, lenght)
    max := 0
    for i, height := range heights {
        if max < height {
            max = height
        }
        maxLeft[i] = max
    }

    max = 0
    for i := lenght - 1; i >= 0; i-- {
        if max < heights[i] {
            max = heights[i]
        }
        maxRight[i] = max
    }

    for i := 0; i < lenght; i++ {
        if maxRight[i] < maxLeft[i] {
            maxLeft[i] = maxRight[i]
        }
    }

    sum := 0
    for i := 0; i < lenght; i++ {
        sum += maxLeft[i] - heights[i]
    }

    return sum
}