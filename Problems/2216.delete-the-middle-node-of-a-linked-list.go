// title: Delete the Middle Node of a Linked List
// timestamp: 2024-04-18 16:10:08
// problemUrl: https://leetcode.com/problems/delete-the-middle-node-of-a-linked-list/
// memory: 13.1 MB
// runtime: 257 ms

/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func deleteMiddle(head *ListNode) *ListNode {
    if head == nil || head.Next == nil {
        return nil
    }
    if head.Next.Next == nil {
        head.Next = nil
        return head
    }
    fastP, slowP := head.Next, head
    for fastP != nil && fastP.Next != nil && fastP.Next.Next != nil {
        slowP = slowP.Next
        fastP = fastP.Next.Next
    }

    slowP.Next = slowP.Next.Next

    return head
}