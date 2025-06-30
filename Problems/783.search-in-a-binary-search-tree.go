// title: Search in a Binary Search Tree
// timestamp: 2024-04-18 00:47:26
// problemUrl: https://leetcode.com/problems/search-in-a-binary-search-tree/
// memory: 6.8 MB
// runtime: 16 ms

/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func searchBST(root *TreeNode, val int) *TreeNode {
    switch {
        case root == nil:
            return nil
        case root.Val == val:
            return root
        case root.Val > val:
            return searchBST(root.Left, val)
        case root.Val < val:
            return searchBST(root.Right, val)
    }

    return nil
}