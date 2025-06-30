# title: Reorder List
# timestamp: 2024-12-19 15:07:20
# problemUrl: https://leetcode.com/problems/reorder-list/
# memory: 23.4 MB
# runtime: 2 ms

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if head == None or head.next == None:
            return head
        
        half, fast = head, head
        while fast.next and fast.next.next:
            half = half.next
            fast = fast.next.next
        tmp = half
        half = half.next
        tmp.next = None

        prev = None
        while half:
            half.next, prev, half = prev, half, half.next
        
        curr = head
        while prev:
            next = curr.next
            curr.next = prev
            prev = prev.next
            curr.next.next = next
            curr = next
            
        return head

        