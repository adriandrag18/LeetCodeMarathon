// title: Smallest String Starting From Leaf
// timestamp: 2024-04-17 20:40:29
// problemUrl: https://leetcode.com/problems/smallest-string-starting-from-leaf/
// memory: 4.5 MB
// runtime: 5 ms

/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
import (
    "fmt"
)

func smallestFromLeaf(root *TreeNode) string {
    res := ""
	dfs(root, "", &res)
	return res
}

func dfs(node *TreeNode, text string, res *string) {
		if node == nil {
			return
		}

		text1 := string(rune(node.Val + 'a')) + text

		if node.Right == nil && node.Left == nil {
			if *res == "" || *res > text1 {
				*res = text1
			}

			return
		}
        
		dfs(node.Left, text1, res)
		dfs(node.Right, text1, res)
}