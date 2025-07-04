# title: IPO
# timestamp: 2025-06-19 22:46:37
# problemUrl: https://leetcode.com/problems/ipo/
# memory: 42.9 MB
# runtime: 265 ms

class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        n = len(profits)
        projects = sorted(zip(capital, profits))
        heap = []
        i = 0
        while i < n:
            cap, profit = projects[i]
            if cap > w:
                break
            heap.append(-profit)
            i += 1
        
        if not heap:
            return w
        
        heapify(heap)
        for _ in range(k):
            if not heap:
                return w
            w -= heappop(heap)
            while i < n:
                cap, profit = projects[i]
                if cap > w:
                    break
                heappush(heap, -profit)
                i += 1
        
        return w