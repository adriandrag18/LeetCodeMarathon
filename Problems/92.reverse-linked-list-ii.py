# title: Reverse Linked List II
# timestamp: 2025-06-11 13:19:01
# problemUrl: https://leetcode.com/problems/reverse-linked-list-ii/
# memory: 17.9 MB
# runtime: 0 ms

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left == right or not head or not head.next:
            return head
        
        last = head if left != 1 else None
        for _ in range(left - 2):
            last = last.next
        
        if last:
            start = last.next
            last.next = None
        else:
            start = head
        i = 0
        prev, curr = None, start
        while curr and i < right - left + 1:
            next = curr.next
            curr.next = prev
            prev, curr = curr, next
            i += 1
        
        start.next = curr
        if last:
            last.next = prev
            return head

        return prev
