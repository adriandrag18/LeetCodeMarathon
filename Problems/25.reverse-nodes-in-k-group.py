# title: Reverse Nodes in k-Group
# timestamp: 2024-12-19 17:58:40
# problemUrl: https://leetcode.com/problems/reverse-nodes-in-k-group/
# memory: 18.5 MB
# runtime: 1 ms

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k == 1:
            return head

        dummy = ListNode(-1)
        prevGroupLast, curr = dummy, head
        while curr:
            fistOfGroup = curr
            prev = None
            i = k
            while i and curr:
                next = curr.next
                curr.next = prev
                prev = curr
                curr = next
                i -= 1
            if i:
                curr, prev = prev, None
                while curr:
                    next = curr.next
                    curr.next = prev
                    prev = curr
                    curr = next
                curr = None

            prevGroupLast.next = prev
            prevGroupLast = fistOfGroup
            
        return dummy.next 
        