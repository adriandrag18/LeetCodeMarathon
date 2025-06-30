// title: Leaf-Similar Trees
// timestamp: 2024-04-14 23:06:13
// problemUrl: https://leetcode.com/problems/leaf-similar-trees/
// memory: 2.9 MB
// runtime: 2 ms

/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

import "fmt"

func leafSimilar(root1 *TreeNode, root2 *TreeNode) bool {
    var root1Leafs, root2Leafs []int

    getLeafs(root1, &root1Leafs)
    getLeafs(root2, &root2Leafs)

    if len(root1Leafs) != len(root2Leafs) {
        return false
    }

    for i, root1Leaf := range root1Leafs {
        if root1Leaf != root2Leafs[i] {
            return false
        }
    }

    fmt.Println(root1Leafs, root2Leafs)

    return true
}

func getLeafs(root *TreeNode, leafs *[]int) {
    if root == nil {
        return
    }

    if root.Left == nil && root.Right == nil {
        *leafs = append(*leafs, root.Val)
        return 
    }

    getLeafs(root.Left, leafs)
    getLeafs(root.Right, leafs)
}