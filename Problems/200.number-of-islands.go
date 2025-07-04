// title: Number of Islands
// timestamp: 2024-04-19 22:09:27
// problemUrl: https://leetcode.com/problems/number-of-islands/
// memory: 6.1 MB
// runtime: 16 ms

func numIslands(grid [][]byte) int {
    g := make([][]int, len(grid))
    for i, line := range grid {
        g[i] = make([]int, len(line))
    }

    counter, unionNo := 1, 0
    for i, line := range grid {
        for j, cell := range line {
            if cell  == '0' {
                continue
            }
            var color int
            if i > 0 && g[i - 1][j] != 0 {
                color = g[i - 1][j]
            }
            if j > 0 && g[i][j - 1] != 0 {
                if color != 0 && color != g[i][j - 1] {
                    color = min(color, g[i][j - 1])
                    union(g, i, j)
                    unionNo++
                } else {
                    color = g[i][j - 1]
                }
            }
            if color == 0 {
                color = counter
                counter++
            }
            g[i][j] = color
        }
    }
    return counter - unionNo - 1
}

func union(g [][]int, i, j int) {
    color := min(g[i - 1][j], g[i][j - 1])
    var oldColor int
    queue := [][2]int{}
    if color == g[i - 1][j] {
        queue = append(queue, [2]int{i, j - 1})
        oldColor = g[i][j - 1]
    } else {
        queue = append(queue, [2]int{i - 1, j})
        oldColor = g[i - 1][j]
    }
    for len(queue) > 0 {
        top := queue[0]
        i, j := top[0], top[1]
        queue = queue[1:]

        g[i][j] = color

        if i > 0 && g[i - 1][j] == oldColor {
            queue = append(queue, [2]int{i - 1, j})
        }
        if j > 0 && g[i][j - 1] == oldColor {
            queue = append(queue, [2]int{i, j - 1})
        }
        if j < len(g[i]) - 1 && g[i][j + 1] == oldColor {
            queue = append(queue, [2]int{i, j + 1})
        }
        if i < len(g) - 1 && g[i + 1][j] == oldColor {
            queue = append(queue, [2]int{i + 1, j})
        }
    }
}