// title: Delete Node in a BST
// timestamp: 2024-04-18 21:25:23
// problemUrl: https://leetcode.com/problems/delete-node-in-a-bst/
// memory: 6.9 MB
// runtime: 14 ms

/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func deleteNode(root *TreeNode, key int) *TreeNode {
    if root == nil {
        return nil
    }

    switch {
    case root.Val == key:
        switch {
        case root.Left == nil && root.Right == nil:
            root = nil
        case root.Left == nil:
            root = root.Right
        case root.Right == nil:
            root = root.Left
        default:
            smallest := getSmallest(root.Right)
            root.Val = smallest
            root.Right = deleteNode(root.Right, smallest)
        }
        return root
    case root.Val < key:
        root.Right = deleteNode(root.Right, key)
    case root.Val > key:
        root.Left = deleteNode(root.Left, key)
    }

    return root
}

func getSmallest(root *TreeNode) int {
    if root.Left == nil {
        return root.Val
    }
    return getSmallest(root.Left)
}