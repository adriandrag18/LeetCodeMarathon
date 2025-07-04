# title: Intersection of Two Linked Lists
# timestamp: 2025-01-04 01:03:51
# problemUrl: https://leetcode.com/problems/intersection-of-two-linked-lists/
# memory: 27.8 MB
# runtime: 95 ms

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        if not headA or not headB:
            return None
        
        p1, p2 = headA, headB
        while p1 != p2:
            if not p1:
                p1 = headB
            else:
                p1 = p1.next
            
            if not p2:
                p2 = headA
            else:
                p2 = p2.next
        
        return p1