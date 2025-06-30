// title: Maximum Twin Sum of a Linked List
// timestamp: 2024-04-18 00:33:30
// problemUrl: https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/
// memory: 13.1 MB
// runtime: 155 ms

/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func pairSum(head *ListNode) int {
    var list []int
    var max int
    for head != nil {
        list = append(list, head.Val)
        head = head.Next
    }
    for i, j := 0, len(list) - 1; i < j; i, j = i + 1, j - 1 {
        sum := list[i] + list[j]
        if max < sum {
            max = sum
        }
    }
    return max
}