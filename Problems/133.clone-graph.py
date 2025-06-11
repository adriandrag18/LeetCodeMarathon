# title: Clone Graph
# timestamp: 2025-01-06 18:49:38
# problemUrl: https://leetcode.com/problems/clone-graph/
# memory: 18.1 MB
# runtime: 40 ms

"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        def dfs(node):
            if node in nodes:
                return nodes[node]
            
            new = Node(node.val)
            nodes[node] = new
            new.neighbors = [dfs(n) for n in node.neighbors]
            
            return new
        
        nodes = {None: None}
        return dfs(node)