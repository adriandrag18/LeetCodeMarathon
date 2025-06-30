# title: Add Two Numbers
# timestamp: 2024-12-19 16:03:10
# problemUrl: https://leetcode.com/problems/add-two-numbers/
# memory: 17.9 MB
# runtime: 7 ms

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode((l1.val + l2.val) % 10)
        carry = (l1.val + l2.val) // 10
        
        curr, l1, l2 = head, l1.next, l2.next
        while l1 and l2:
            curr.next = ListNode((l1.val + l2.val + carry) % 10)
            carry = (l1.val + l2.val + carry) // 10
            curr = curr.next
            l1, l2 = l1.next, l2.next

        while l1:
            curr.next = ListNode((l1.val + carry) % 10)
            carry = (l1.val + carry) // 10
            curr = curr.next
            l1 = l1.next
        
        while l2:
            curr.next = ListNode((l2.val + carry) % 10)
            carry = (l2.val + carry) // 10
            curr = curr.next
            l2 = l2.next
        
        if carry:
            curr.next = ListNode(carry)
        
        return head