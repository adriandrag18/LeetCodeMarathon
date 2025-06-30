// title: Maximum Level Sum of a Binary Tree
// timestamp: 2024-04-18 21:42:40
// problemUrl: https://leetcode.com/problems/maximum-level-sum-of-a-binary-tree/
// memory: 7.5 MB
// runtime: 109 ms

/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func maxLevelSum(root *TreeNode) int {
    if root == nil {
        return 0
    }

    var level, newLevel []*TreeNode
    level = []*TreeNode{root}

    var max, maxDepth, depth int
    max, depth = -1000000000, 1
    for len(level) != 0 {
        s := sum(level)
        if max < s {
            max = s
            maxDepth = depth
        }
        
        for _, node := range level {
            if node.Left != nil {
                newLevel = append(newLevel, node.Left)
            }
            if node.Right != nil {
                newLevel = append(newLevel, node.Right)
            }
        }
        level = newLevel
        newLevel = nil
        depth++
    }

    return maxDepth
}

func sum(l []*TreeNode) (sum int) {
    for _, node := range l {
        sum += node.Val
    }
    return sum
}