// title: Minimum Falling Path Sum II
// timestamp: 2024-04-26 13:58:52
// problemUrl: https://leetcode.com/problems/minimum-falling-path-sum-ii/
// memory: 6.4 MB
// runtime: 18 ms

import (
	"math"
)

type Triplet struct {
	minSum       int
	secondMinSum int
	minSumIndex  int
}

func minFallingPathSum(grid [][]int) int {
	return minFallingPathSumHelper(0, grid).minSum
}

func minFallingPathSumHelper(row int, grid [][]int) Triplet {
	if row == len(grid) {
		return Triplet{0, 0, 0}
	}

	nextRowTriplet := minFallingPathSumHelper(row+1, grid)
	currentTriplet := Triplet{math.MaxInt32, math.MaxInt32, -1}

	for col := 0; col < len(grid[0]); col++ {
		var value int
		if col != nextRowTriplet.minSumIndex {
			value = grid[row][col] + nextRowTriplet.minSum
		} else {
			value = grid[row][col] + nextRowTriplet.secondMinSum
		}

		if value <= currentTriplet.minSum {
			currentTriplet.secondMinSum = currentTriplet.minSum
			currentTriplet.minSum = value
			currentTriplet.minSumIndex = col
		} else if value < currentTriplet.secondMinSum {
			currentTriplet.secondMinSum = value
		}
	}

	return currentTriplet
}
