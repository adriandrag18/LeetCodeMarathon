// title: Find the Difference of Two Arrays
// timestamp: 2024-04-18 12:46:52
// problemUrl: https://leetcode.com/problems/find-the-difference-of-two-arrays/
// memory: 6.9 MB
// runtime: 23 ms

func findDifference(nums1 []int, nums2 []int) [][]int {
    map1, map2 := make(map[int]struct{}), make(map[int]struct{})

    for _, num := range nums1 {
        map1[num] = struct{}{}
    }
    for _, num := range nums2 {
        map2[num] = struct{}{}
    }

    answer := make([][]int, 2)
    for num := range map1 {
        if _, ok := map2[num]; !ok {
            answer[0] = append(answer[0], num)
        }
    }
    for num := range map2 {
        if _, ok := map1[num]; !ok {
            answer[1] = append(answer[1], num)
        }
    }

    return answer
}