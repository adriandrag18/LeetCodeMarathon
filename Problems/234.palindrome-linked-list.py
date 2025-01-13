# title: Palindrome Linked List
# timestamp: 2025-01-13 19:12:24
# problemUrl: https://leetcode.com/problems/palindrome-linked-list/
# memory: 39.7 MB
# runtime: 223 ms

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return True
        
        curr, reversed = head, ListNode(-1)
        while curr:
            reversed = ListNode(curr.val, reversed)
            curr = curr.next
        
        curr, currR = head, reversed
        while curr:
            if curr.val != currR.val:
                return False
            curr = curr.next
            currR = currR.next
        
        return True