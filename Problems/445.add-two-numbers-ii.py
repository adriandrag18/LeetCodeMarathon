# title: Add Two Numbers II
# timestamp: 2025-06-11 13:04:07
# problemUrl: https://leetcode.com/problems/add-two-numbers-ii/
# memory: 17.9 MB
# runtime: 4 ms

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def reverse(head):
            if not head or not head.next:
                return head
            
            prev, curr = None, head
            while curr:
                next = curr.next
                curr.next = prev
                prev, curr = curr, next
                
            return prev

        l1, l2 = reverse(l1), reverse(l2)
        curr = head = ListNode()
        carry = 0
        while l1 or l2:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            carry, val = divmod(val1 + val2 + carry, 10)
            curr.next = ListNode(val)
            l1, l2, curr = l1.next if l1 else None, l2.next if l2 else None, curr.next
            
        if carry:
            curr.next = ListNode(carry)
            
        return reverse(head.next)