// title: Find All Groups of Farmland
// timestamp: 2024-04-20 23:04:46
// problemUrl: https://leetcode.com/problems/find-all-groups-of-farmland/
// memory: 33.8 MB
// runtime: 119 ms

import (
    "fmt"
)

func findFarmland(land [][]int) [][]int {
    var result [][]int
    for i := 0; i < len(land); i++ {
        for j := 0; j < len(land[0]); j++ {
            if land[i][j] != 1 {
                continue
            }
            if (i > 0 && land[i-1][j] == 2) || (j > 0 && land[i][j-1] == 2) {
                land[i][j] = 2
                continue
            }
            // fmt.Print(i, j, " ")
            res := []int{i, j}
            oldI := i
            for j < len(land[0]) && land[i][j] == 1 {
                land[i][j] = 2
                j++
            }
            j--
            i++
            for i < len(land) && land[i][j] == 1 {
                land[i][j] = 2
                i++
            }
            i--
            res = append(res, i, j)
            result = append(result, res)
            i = oldI
            // fmt.Println(i, j)
        }
    } 
    return result
}