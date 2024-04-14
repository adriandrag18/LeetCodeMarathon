// title: Sum of Left Leaves
// timestamp: 2024-04-14 20:44:42
// problemUrl: https://leetcode.com/problems/sum-of-left-leaves/
// memory: 2.8 MB
// runtime: 0 ms

/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func sumOfLeftLeaves(root *TreeNode) int {
    var sum = 0
    
    if root.Left != nil  {
        if root.Left.Left == nil && root.Left.Right == nil {
            sum += root.Left.Val
        } else {
            sum += sumOfLeftLeaves(root.Left)
        }
    }
        
    if root.Right != nil  {
        sum += sumOfLeftLeaves(root.Right)
    }

    return sum
}