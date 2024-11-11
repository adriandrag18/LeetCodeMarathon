# title: Reverse Linked List
# timestamp: 2024-11-11 22:21:55
# problemUrl: https://leetcode.com/problems/reverse-linked-list/
# memory: 17.4 MB
# runtime: 0 ms

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        prev, curr = None, head
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        
        return prev