// title: Validate Binary Search Tree
// timestamp: 2024-04-14 20:24:33
// problemUrl: https://leetcode.com/problems/validate-binary-search-tree/
// memory: 5.4 MB
// runtime: 0 ms

/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func isValidBST(root *TreeNode) bool {
    valid, _, _ := validBST(root)
    return valid
}

func validBST(root *TreeNode) (valid bool, min int, max int) {
    min, max = 2147483647, -2147483648

    if root == nil {
        return true, min, max
    }
    
    if root.Left != nil {
        if root.Left.Val >= root.Val {
            return false, min, max
        }
        valid, minL, maxL := validBST(root.Left)
        if !valid || maxL >= root.Val {
            return false, min, max
        }
        if min > minL {
            min = minL
        }
        if max < maxL {
            max = maxL
        }
    } else {
        min, max = root.Val, root.Val
    }

    if root.Right != nil {
        if root.Val >= root.Right.Val {
            return false, min, max
        }
        valid, minR, maxR := validBST(root.Right)
        if !valid || minR <= root.Val {
            return false, min, max
        }
        if min > minR {
            min = minR
        }
        if max < maxR {
            max = maxR
        }
    } else {
        max = root.Val
    }

    return true, min, max
}