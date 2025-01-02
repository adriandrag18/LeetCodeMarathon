# title: Find Median from Data Stream
# timestamp: 2025-01-03 00:49:04
# problemUrl: https://leetcode.com/problems/find-median-from-data-stream/
# memory: 39.5 MB
# runtime: 175 ms

class MedianFinder:

    def __init__(self):
        # self.list = SortedList([])

        self.minHeap = []
        heapq.heapify(self.minHeap)
        self.maxHeap = []
        heapq.heapify(self.maxHeap)

    def addNum(self, num: int) -> None:
        # self.list.add(nums)
        
        heappush(self.maxHeap, -num)
        heappush(self.minHeap, -heappop(self.maxHeap))
        while len(self.minHeap) > len(self.maxHeap):
            heappush(self.maxHeap, -heappop(self.minHeap))

    def findMedian(self) -> float:
        # if len(self.list) % 2 == 1:
        #     return self.list[len(self.list) // 2]
        
        # return (self.list[len(self.list) // 2 - 1] + self.list[len(self.list) // 2]) / 2
        
        if len(self.minHeap) == len(self.maxHeap):
            minEl = heappop(self.minHeap)
            maxEl = -heappop(self.maxHeap)
            heappush(self.minHeap, minEl)
            heappush(self.maxHeap, -maxEl)
            return (minEl + maxEl) / 2
        
        el = -heappop(self.maxHeap)
        heappush(self.maxHeap, -el)
        return el
        

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()