// title: Find if Path Exists in Graph
// timestamp: 2024-04-21 23:44:45
// problemUrl: https://leetcode.com/problems/find-if-path-exists-in-graph/
// memory: 83.4 MB
// runtime: 296 ms

import "fmt"

func validPath(n int, e [][]int, source int, destination int) bool {
    if source == destination {
        return true
    }
    
    edges := make([][]int, n)
    for _, edge := range e {
        edges[edge[0]] = append(edges[edge[0]], edge[1])
        edges[edge[1]] = append(edges[edge[1]], edge[0])
    }

    seen := make(map[int]bool, n)
    for i := range n {
        seen[i] = false
    }

    var dfs func(neib []int) bool
    dfs = func(neib []int) bool {
        for _, node := range neib {
            if node == destination {
                return true
            }
            if !seen[node] {
                seen[node] = true
                if dfs(edges[node]) {
                    return true
                }
            }
        }
        return false
    }

    seen[source] = true
    return dfs(edges[source])
}