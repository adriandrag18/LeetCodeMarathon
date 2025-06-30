# title: Reorder Routes to Make All Paths Lead to the City Zero
# timestamp: 2025-01-06 16:56:55
# problemUrl: https://leetcode.com/problems/reorder-routes-to-make-all-paths-lead-to-the-city-zero/
# memory: 40.9 MB
# runtime: 150 ms

class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        adjList = [[] for _ in range(n)]
        for a, b in connections:
            adjList[a].append((b, 2))
            adjList[b].append((a, 1))

        seen = [False] * n
        count, seen[0], queue = 0, True, deque([(0, 0)])
        while queue:
            n, depth = queue.popleft()
            for node, typ in adjList[n]:
                if seen[node]:
                    continue
                queue.append((node, depth + 1))
                seen[node] = True
                if typ == 2:
                    count += 1
        
        return count