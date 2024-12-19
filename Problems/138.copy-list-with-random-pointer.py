# title: Copy List with Random Pointer
# timestamp: 2024-12-19 15:52:44
# problemUrl: https://leetcode.com/problems/copy-list-with-random-pointer/
# memory: 18.6 MB
# runtime: 34 ms

"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        def toString(node):
            if not node:
                return 'null'
            random = node.random.val if node.random else 'null'
            return f'[{node.val}, {random}] -> {toString(node.next)}'
            
        
        if not head:
            return head

        map = {None: None}
        curr = head
        while curr:
            if curr not in map:
                map[curr] = Node(curr.val)
            node = map[curr]
            
            if curr.next not in map:
                map[curr.next] = Node(curr.next.val)
            node.next = map[curr.next]
            
            if curr.random not in map:
                map[curr.random] = Node(curr.random.val)
            node.random = map[curr.random]
            # print(toString(node))
            curr = curr.next

        return map[head]