// title: Rotting Oranges
// timestamp: 2024-04-20 23:51:40
// problemUrl: https://leetcode.com/problems/rotting-oranges/
// memory: 3.1 MB
// runtime: 3 ms

import "fmt"

func orangesRotting(grid [][]int) int {
    var queue [][2]int
    for i, line := range grid {
        for j, cell := range line {
            if cell == 2 {
                queue = append(queue, [2]int{i, j})
            }
        }
    }

    var count int
    var newQueue [][2]int
    for len(queue) > 0 {
        for _, node := range queue {
            i, j := node[0], node[1]
            if i > 0 && grid[i-1][j] == 1 {
                grid[i-1][j] = 2
                newQueue = append(newQueue, [2]int{i-1, j})
            }
            if j > 0 && grid[i][j-1] == 1 {
                grid[i][j-1] = 2
                newQueue = append(newQueue, [2]int{i, j-1})
            }
            if i < len(grid)-1 && grid[i+1][j] == 1 {
                grid[i+1][j] = 2
                newQueue = append(newQueue, [2]int{i+1, j})
            }
            if j < len(grid[i])-1 && grid[i][j+1] == 1 {
                grid[i][j+1] = 2
                newQueue = append(newQueue, [2]int{i, j+1})
            }
        }
        fmt.Println(count, queue, newQueue)
        queue = newQueue
        newQueue = nil
        count++
    }

    for _, line := range grid {
        for _, cell := range line {
            if cell == 1 {
                return -1
            }
        }
    }
    
    return max(0, count - 1)
}