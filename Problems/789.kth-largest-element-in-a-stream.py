# title: Kth Largest Element in a Stream
# timestamp: 2025-01-02 18:30:45
# problemUrl: https://leetcode.com/problems/kth-largest-element-in-a-stream/
# memory: 23.6 MB
# runtime: 27 ms

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = nums
        heapq.heapify(self.heap)

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)
       
        while len(self.heap) > self.k:
            heapq.heappop(self.heap)
        
        return self.heap[0]



# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)