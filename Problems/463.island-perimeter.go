// title: Island Perimeter
// timestamp: 2024-04-18 12:18:26
// problemUrl: https://leetcode.com/problems/island-perimeter/
// memory: 8.1 MB
// runtime: 87 ms

import (
    "fmt"
)

func islandPerimeter(grid [][]int) int {
    per := 4
    i, j := findFirstSquare(grid)
    var queue [][2]int
    seen := make(map[[2]int]struct{})
    seen[[2]int{i, j}] = struct{}{}

    if j + 1 < len (grid[0]) && grid[i][j + 1] == 1 {
        queue = append(queue, [2]int{i, j + 1})
        seen[[2]int{i, j + 1}] = struct{}{}
        per--
    }
    if i + 1 < len (grid) && grid[i + 1][j] == 1 {
        queue = append(queue, [2]int{i + 1, j})
        seen[[2]int{i + 1, j}] = struct{}{}
        per--
    }

    for len(queue) > 0 {
        top := queue[0]
        queue = queue[1:]
        i, j := top[0], top[1]
        per += 4

        _, ok := seen[[2]int{i - 1, j}]
        if i - 1 >=0 && grid[i - 1][j] == 1 {
            if !ok {
                seen[[2]int{i - 1, j}] = struct{}{}
                queue = append(queue, [2]int{i - 1, j})
            }
            per--
        }

        _, ok = seen[[2]int{i, j - 1}]
        if j - 1 >= 0 && grid[i][j - 1] == 1 {
            if !ok {
                seen[[2]int{i, j - 1}] = struct{}{}
                queue = append(queue, [2]int{i, j - 1})
            }
            per--
        }  

        _, ok = seen[[2]int{i, j + 1}]
        if j + 1 < len (grid[0]) && grid[i][j + 1] == 1 {
            if !ok {
                seen[[2]int{i, j + 1}] = struct{}{}
                queue = append(queue, [2]int{i, j + 1})
            }
            per--
        }

        _, ok = seen[[2]int{i + 1, j}]
        if i + 1 < len (grid) && grid[i + 1][j] == 1 {
            if !ok {
                seen[[2]int{i + 1, j}] = struct{}{}
                queue = append(queue, [2]int{i + 1, j})
            }
            per--
        }  
    }
    return per
}
    
func findFirstSquare(grid [][]int) (int, int) {
    for i, row := range grid {
        for j, cell := range row {
            if cell == 1 {
                return i, j
            }
        }
    }
    return -1, -1
}