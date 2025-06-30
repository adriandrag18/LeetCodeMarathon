// title: Non-overlapping Intervals
// timestamp: 2024-04-23 16:48:22
// problemUrl: https://leetcode.com/problems/non-overlapping-intervals/
// memory: 16.8 MB
// runtime: 179 ms

import (
    "sort"
)

func eraseOverlapIntervals(intervals [][]int) int {
    sort.Slice(intervals, func(i, j int) bool {
        return intervals[i][0] < intervals[j][0]
    })

    const removed = -100000
    var count int
    for i, j := 0, 1; j < len(intervals); {
        if intervals[i][0] == removed {
            i++
            continue
        }
        if intervals[j][0] == removed {
            j++
            continue
        }
        if intervals[j][0] >= intervals[i][1] {
            i++
            j++
            continue
        }
        //remove one
        count++
        if intervals[i][1] < intervals[j][1] {
            intervals[j][0] = removed
            j++
            continue
        }
        intervals[i][0] = removed
        i++
        j++
    }

    return count
}