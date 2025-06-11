// title: Unique Paths
// timestamp: 2024-04-23 15:33:55
// problemUrl: https://leetcode.com/problems/unique-paths/
// memory: 2.4 MB
// runtime: 1 ms

func uniquePaths(m int, n int) int {
    grid := make([][]int, m)
    for i := range m {
        grid[i] = make([]int, n)
    }
    for i := range m {
        grid[i][0] = 1
    }
    for i := range n {
        grid[0][i] = 1
    }
    for i := 1; i < m; i++ {
        for j := 1; j < n; j++ {
            grid[i][j] = grid[i-1][j] + grid[i][j-1]
        }
    }
    return grid[m-1][n-1]
}