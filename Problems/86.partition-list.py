# title: Partition List
# timestamp: 2025-01-15 12:25:05
# problemUrl: https://leetcode.com/problems/partition-list/
# memory: 17.7 MB
# runtime: 0 ms

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        less, greater = ListNode(-1), ListNode(-1)
        curr, l, g = head, less, greater
        while curr:
            next = curr.next
            curr.next = None
            if curr.val < x:
                l.next, l = curr, curr
            else:
                g.next, g = curr, curr

            curr = next
        
        l.next = greater.next
        
        return less.next