# title: Odd Even Linked List
# timestamp: 2024-12-28 02:34:09
# problemUrl: https://leetcode.com/problems/odd-even-linked-list/
# memory: 19 MB
# runtime: 0 ms

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next or not head.next.next:
            return head
        
        oddHead = ListNode(-1)
        even, odd = head, oddHead 
        while even.next and even.next.next:
            odd.next = even.next
            even.next = even.next.next
            
            odd = odd.next
            even = even.next

        odd.next = even.next
        even.next = oddHead.next
        return head