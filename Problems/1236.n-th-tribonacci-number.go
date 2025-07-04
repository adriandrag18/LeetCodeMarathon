// title: N-th Tribonacci Number
// timestamp: 2024-04-24 11:03:58
// problemUrl: https://leetcode.com/problems/n-th-tribonacci-number/
// memory: 2.2 MB
// runtime: 1 ms

func tribonacci(n int) int {
    switch n {
        case 0:
            return 0
        case 1:
            return 1
        case 2:
            return 1
    }
    
    trifib := make([]int, n + 1)
    trifib[0], trifib[1], trifib[2] = 0, 1, 1
    
    for i := 3; i <= n; i++ {
        trifib[i] = trifib[i - 1] + trifib[i - 2] + trifib[i - 3]
    }

    return trifib[n]
}