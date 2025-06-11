# title: Remove Duplicates from Sorted List II
# timestamp: 2025-06-11 13:28:49
# problemUrl: https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/
# memory: 17.7 MB
# runtime: 0 ms

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        dummy = ListNode(-1000, head)
        prev, curr = dummy, head
        while curr and curr.next:
            if curr.val == curr.next.val:
                target = curr.val
                while curr and curr.val == target:
                    prev.next = curr = curr.next
                continue
            prev, curr = curr, curr.next

        return dummy.next