# title: Remove Nth Node From End of List
# timestamp: 2024-12-19 15:16:14
# problemUrl: https://leetcode.com/problems/remove-nth-node-from-end-of-list/
# memory: 17.6 MB
# runtime: 0 ms

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        fast = head
        while n and fast:
            fast = fast.next
            n -= 1
        
        if n:
            return head
        
        dummy = ListNode(-1, head)
        curr = dummy
        while fast:
            curr = curr.next
            fast = fast.next
        
        curr.next = curr.next.next
        return dummy.next