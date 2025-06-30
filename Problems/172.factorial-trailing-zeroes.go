// title: Factorial Trailing Zeroes
// timestamp: 2024-04-14 20:37:57
// problemUrl: https://leetcode.com/problems/factorial-trailing-zeroes/
// memory: 2.2 MB
// runtime: 0 ms

func trailingZeroes(n int) int {
    var numberOfFives = 0
    for n > 0 {
        n /= 5
        numberOfFives += n;
    }
    return numberOfFives
}