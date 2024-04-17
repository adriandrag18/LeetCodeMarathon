// title: Kids With the Greatest Number of Candies
// timestamp: 2024-04-18 01:20:59
// problemUrl: https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/
// memory: 2.5 MB
// runtime: 0 ms

func kidsWithCandies(candies []int, extraCandies int) []bool {
    var max int 
    for _, c := range candies {
        if max < c {
            max = c
        }
    }
    res := make([]bool, len(candies))
    for i, c := range candies {
        if c + extraCandies < max {
            res[i] = false
            continue
        }
        res[i] = true
    }
    return res
}