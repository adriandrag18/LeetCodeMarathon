// title: Add One Row to Tree
// timestamp: 2024-04-16 19:07:40
// problemUrl: https://leetcode.com/problems/add-one-row-to-tree/
// memory: 5.9 MB
// runtime: 6 ms

/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func addOneRow(root *TreeNode, val int, depth int) *TreeNode {
    if depth == 1 {
        return &TreeNode{Val: val, Left: root}
    } 
    addOneRowInplace(root, val, depth)
    
    return root
}

func addOneRowInplace(root *TreeNode, val int, depth int) {
    if depth == 2 {
        root.Left = &TreeNode{Val: val, Left: root.Left}
        root.Right = &TreeNode{Val: val, Right: root.Right}
        return
    }

    if root.Left != nil {
        _ = addOneRow(root.Left, val, depth - 1)
    }
    if root.Right != nil {
        _ = addOneRow(root.Right, val, depth - 1)
    }
    
    return
}