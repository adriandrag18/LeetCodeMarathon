// title: Find the Highest Altitude
// timestamp: 2024-04-18 12:35:49
// problemUrl: https://leetcode.com/problems/find-the-highest-altitude/
// memory: 2.3 MB
// runtime: 2 ms

func largestAltitude(gain []int) int {
    var max, sum int

    for _, g := range gain {
        sum += g
        if max < sum {
            max = sum
        }
    }

    return max
}