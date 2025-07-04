// title: Unique Number of Occurrences
// timestamp: 2024-04-18 12:51:34
// problemUrl: https://leetcode.com/problems/unique-number-of-occurrences/
// memory: 2.6 MB
// runtime: 2 ms

func uniqueOccurrences(arr []int) bool {
    occ := make(map[int]int)
    for _, num := range arr {
        if _, ok := occ[num]; !ok {
            occ[num] = 0
        }
        occ[num]++
    }

    unique := make(map[int]struct{})
    for _, o := range occ {
        if _, ok := unique[o]; ok {
            return false
        }
        unique[o] = struct{}{}
    }
    
    return true
}