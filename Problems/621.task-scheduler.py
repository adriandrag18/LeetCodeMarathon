# title: Task Scheduler
# timestamp: 2025-01-02 19:33:44
# problemUrl: https://leetcode.com/problems/task-scheduler/
# memory: 19.2 MB
# runtime: 14 ms

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = {}
        for t in tasks:
            freq[t] = freq.get(t, 0) + 1
        
        heap = [-count for count in freq.values()]
        heapq.heapify(heap)

        maxFrequency = -heap[0]
        num = 0
        while heap:
            if -heapq.heappop(heap) != maxFrequency: 
                break
            num += 1

        maxInterval = num + (n + 1) * (maxFrequency - 1)
        
        return max(len(tasks), maxInterval)
