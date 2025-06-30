# title: Sort List
# timestamp: 2025-01-15 11:55:18
# problemUrl: https://leetcode.com/problems/sort-list/
# memory: 32.8 MB
# runtime: 223 ms

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1
       
        if list1.val > list2.val:
            return self.mergeTwoLists(list2, list1)
        
        res, list1, curr = list1, list1.next, list1
        curr = res
        while list1 and list2:
            if list1.val < list2.val:
                curr.next, list1 = list1, list1.next
                curr = curr.next
                continue

            curr.next, list2 = list2, list2.next
            curr = curr.next

        while list1:
            curr.next, list1, curr = list1, list1.next, list1

        while list2:
            curr.next, list2, curr = list2, list2.next, list2
        
        return res
    
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow, fast = head, head
        while fast and fast.next:
            fast = fast.next.next
            if not fast or not fast.next: 
                break
            slow = slow.next
        # print(slow)
        half = slow.next if slow else None
        if slow != fast:
            slow.next = None
            head = self.sortList(head)
            half = self.sortList(half)
        
        return self.mergeTwoLists(head, half)