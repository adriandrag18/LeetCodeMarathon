# title: Rotate List
# timestamp: 2025-01-15 12:15:54
# problemUrl: https://leetcode.com/problems/rotate-list/
# memory: 18.1 MB
# runtime: 0 ms

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return None
        
        n, curr = 1, head
        while curr.next:
            n += 1
            curr = curr.next
        
        k %= n
        if not k:
            return head
        
        last, curr = curr, head
        for _ in range(n - k - 1):
            curr = curr.next
        
        last.next = head
        head, curr.next = curr.next, None

        return head
        

