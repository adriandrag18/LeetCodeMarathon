// title: Add Two Numbers
// timestamp: 2024-04-24 00:32:31
// problemUrl: https://leetcode.com/problems/add-two-numbers/
// memory: 4.3 MB
// runtime: 0 ms

/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func addTwoNumbers(l1 *ListNode, l2 *ListNode) *ListNode {
    var carry int
    for p1, p2 := l1, l2; p1 != nil || p2 != nil; p1, p2 = p1.Next, p2.Next {
        val := carry
        if p1 != nil {
            val += p1.Val
        }
        if p2 != nil {
            val += p2.Val
        }
        p1.Val = val % 10
        carry = val / 10
        if p1.Next == nil && (carry != 0 || p2.Next != nil) {
            p1.Next = &ListNode{}
        }
        if p2.Next == nil && p1.Next != nil {
            p2.Next = &ListNode{}
        }
    }

    return l1
}