// title: Minimum Number of Arrows to Burst Balloons
// timestamp: 2024-04-23 17:05:37
// problemUrl: https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/
// memory: 16.4 MB
// runtime: 211 ms

import (
    "sort"
)

func findMinArrowShots(points [][]int) int {
    if len(points) == 0 {
        return 0
    }

    sort.Slice(points, func(i, j int) bool {
        return points[i][0] < points[j][0]
    })

    count := 1
    overlap := points[0]
    for i := 1; i < len(points); i++ {
        if overlap[1] < points[i][0] {
            count++
            overlap = points[i]
            continue
        }
        overlap[0] = max(overlap[0], points[i][0])
        overlap[1] = min(overlap[1], points[i][1])
    }
    
    return count
}

func max(a, b int)int{
    if a > b{
        return a
    }else{
        return b
    }
}

func min(a, b int)int{
    if a > b{
        return b
    }else{
        return a
    }
}