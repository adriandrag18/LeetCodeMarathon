// title: Count Good Nodes in Binary Tree
// timestamp: 2024-04-19 23:48:39
// problemUrl: https://leetcode.com/problems/count-good-nodes-in-binary-tree/
// memory: 11 MB
// runtime: 68 ms

/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func goodNodes(root *TreeNode) int {
    return good(root.Left, root.Val) + good(root.Right, root.Val) + 1
}

func good(root *TreeNode, m int) int {
    if root == nil {
        return 0
    }

    if m <= root.Val {
        return good(root.Left, root.Val) + good(root.Right, root.Val) + 1
    }
    return good(root.Left, m) + good(root.Right, m)
}