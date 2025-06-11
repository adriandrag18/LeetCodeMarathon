# title: Last Stone Weight
# timestamp: 2025-01-02 18:35:18
# problemUrl: https://leetcode.com/problems/last-stone-weight/
# memory: 17.7 MB
# runtime: 0 ms

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-n for n in stones]
        heapq.heapify(heap)
        while len(heap) > 1:
            x, y = heapq.heappop(heap), heapq.heappop(heap)
            if x < y:
                heapq.heappush(heap, x - y)
        
        return -heap[0] if heap else 0
