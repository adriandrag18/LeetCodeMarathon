# title: Most Beautiful Item for Each Query
# timestamp: 2024-11-12 14:47:53
# problemUrl: https://leetcode.com/problems/most-beautiful-item-for-each-query/
# memory: 65.8 MB
# runtime: 164 ms

class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        items.sort()
        queries = sorted([(q, i) for i, q in enumerate(queries)])
        
        m, j, res = 0, 0, [0] * len(queries)
        for q, i in queries:
            while j < len(items) and items[j][0] <= q: 
                m = max(m, items[j][1])
                j += 1
            res[i] = m
            
        return res
