// title: Maximum Depth of Binary Tree
// timestamp: 2024-04-18 00:49:56
// problemUrl: https://leetcode.com/problems/maximum-depth-of-binary-tree/
// memory: 4.5 MB
// runtime: 0 ms

/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func maxDepth(root *TreeNode) int {
    if root == nil {
        return 0
    }

    return max(maxDepth(root.Left), maxDepth(root.Right)) + 1
}

func max(a, b int) int {
    if a < b {
        return b
    }
    return a
}