# title: Maximum Average Pass Ratio
# timestamp: 2025-01-02 12:34:34
# problemUrl: https://leetcode.com/problems/maximum-average-pass-ratio/
# memory: 54.9 MB
# runtime: 1171 ms

class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        def heapElement(passStudents, totalStudents):
            return (passStudents / totalStudents - (passStudents + 1) / (totalStudents + 1), passStudents, totalStudents)
        
        classes.sort(key=lambda x: heapElement(*x)[0])
        heap = [heapElement(passStudents, totalStudents) for passStudents, totalStudents in classes]
        heapq.heapify(heap)
        
        while extraStudents > 0:
            _, passStudents, totalStudents = heapq.heappop(heap)
            passStudents += 1
            totalStudents += 1
            extraStudents -= 1

            heapq.heappush(heap, heapElement(passStudents, totalStudents))

        return sum([c[1] / c[2] for c in heap]) / len(heap)
