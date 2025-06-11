// title: Sum Root to Leaf Numbers
// timestamp: 2024-04-15 16:29:13
// problemUrl: https://leetcode.com/problems/sum-root-to-leaf-numbers/
// memory: 2.4 MB
// runtime: 1 ms

/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func sumNumbers(root *TreeNode) int {
    return sumLeafs(root, 0)
}

func sumLeafs(root *TreeNode, base int) int {
    if root == nil {
        return 0
    }

    sum := base * 10 + root.Val
    if root.Left == nil && root.Right == nil {
        return sum
    }
    
    return sumLeafs(root.Left, sum) + sumLeafs(root.Right, sum)
}