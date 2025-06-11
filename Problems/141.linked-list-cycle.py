# title: Linked List Cycle
# timestamp: 2024-12-19 16:05:47
# problemUrl: https://leetcode.com/problems/linked-list-cycle/
# memory: 19.8 MB
# runtime: 48 ms

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        
        slow, fast = head, head
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return True
        
        return False