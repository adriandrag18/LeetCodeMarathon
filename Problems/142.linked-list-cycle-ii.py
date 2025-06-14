# title: Linked List Cycle II
# timestamp: 2025-06-06 16:23:05
# problemUrl: https://leetcode.com/problems/linked-list-cycle-ii/
# memory: 19.6 MB
# runtime: 43 ms

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
            if fast == slow:
                while head != slow:
                    head, slow = head.next, slow.next
                return slow
        
        return None