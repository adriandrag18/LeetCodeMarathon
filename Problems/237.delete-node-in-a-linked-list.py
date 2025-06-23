# title: Delete Node in a Linked List
# timestamp: 2025-06-23 13:30:03
# problemUrl: https://leetcode.com/problems/delete-node-in-a-linked-list/
# memory: 17.8 MB
# runtime: 36 ms

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        
        node.val = node.next.val
        node.next = node.next.next