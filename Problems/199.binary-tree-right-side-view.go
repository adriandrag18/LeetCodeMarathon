// title: Binary Tree Right Side View
// timestamp: 2024-04-18 21:37:26
// problemUrl: https://leetcode.com/problems/binary-tree-right-side-view/
// memory: 2.6 MB
// runtime: 0 ms

/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func rightSideView(root *TreeNode) []int {
    if root == nil {
        return nil
    }

    var level, newLevel []*TreeNode
    level = []*TreeNode{root}

    var view []int
    for len(level) != 0 {
        view = append(view, level[len(level) - 1].Val)
        
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
    }

    return view
}