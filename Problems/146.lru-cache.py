# title: LRU Cache
# timestamp: 2024-12-19 16:55:28
# problemUrl: https://leetcode.com/problems/lru-cache/
# memory: 78.8 MB
# runtime: 166 ms

class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev, self.next = None, None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.map = {}
        self.left, self.right = Node(-1, 0), Node(-1, 0)
        self.left.next, self.right.prev = self.right, self.left

    def remove(self, node):
        node.prev.next, node.next.prev = node.next, node.prev
    
    def insert(self, node):
        node.prev, node.next = self.right.prev, self.right
        self.right.prev = node.prev.next = node

    def get(self, key: int) -> int:
        if key not in self.map:
            return -1
        
        node = self.map[key]
        self.remove(node)
        self.insert(node)

        return node.val
        

    def put(self, key: int, value: int) -> None:
        if key in self.map:
            self.remove(self.map[key])
        
        node = Node(key, value)
        self.insert(node)
        self.map[key] = node

        if len(self.map) > self.capacity:
            key = self.left.next.key
            self.remove(self.left.next)
            self.map.pop(key)
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)