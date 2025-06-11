# title: Insertion Sort List
# timestamp: 2025-01-15 12:10:05
# problemUrl: https://leetcode.com/problems/insertion-sort-list/
# memory: 18.8 MB
# runtime: 400 ms

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        
        dummy = ListNode(-1, head)
        curr, head.next = head.next, None
        while curr:
            next = curr.next
            sortCurr = dummy
            while sortCurr.next:
                if curr.val >= sortCurr.next.val:
                    sortCurr = sortCurr.next
                    continue
                sortCurr.next, curr.next = curr, sortCurr.next
                break
            else:
                sortCurr.next, curr.next = curr, None
            curr = next
        
        return dummy.next