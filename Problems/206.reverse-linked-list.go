// title: Reverse Linked List
// timestamp: 2024-04-18 00:41:35
// problemUrl: https://leetcode.com/problems/reverse-linked-list/
// memory: 2.7 MB
// runtime: 2 ms

/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func reverseList(head *ListNode) *ListNode {
    if head == nil {
        return nil
    }
    var rev *ListNode 
    for head != nil {
        next := head.Next
        head.Next = rev
        rev = head
        head = next
    }
    return rev
}