# title: Swap Nodes in Pairs
# timestamp: 2025-01-15 11:40:04
# problemUrl: https://leetcode.com/problems/swap-nodes-in-pairs/
# memory: 18 MB
# runtime: 0 ms

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        dummy = ListNode(-1, head)
        prev, curr = dummy, head
        while curr and curr.next:
            second, third = curr.next, curr.next.next
            prev.next = second
            second.next = curr
            curr.next = third
            prev, curr = curr, third
        
        return dummy.next