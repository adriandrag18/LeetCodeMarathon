# title: Pacific Atlantic Water Flow
# timestamp: 2025-06-20 11:04:08
# problemUrl: https://leetcode.com/problems/pacific-atlantic-water-flow/
# memory: 19.1 MB
# runtime: 27 ms

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m, n = len(heights), len(heights[0])
        dir = [(-1, 0), (0, -1), (0, 1), (1, 0)]
        def bfs(queue, seen):
            while queue:
                i, j = queue.popleft()
                if (i, j) in seen:
                    continue
                seen.add((i, j))
                for di, dj in dir:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < m and 0 <= nj < n and heights[i][j] <= heights[ni][nj]:
                        queue.append((ni, nj))
            

        # bfs from all cells conected to the pacific
        # keep track of seen nodes
        queue = deque([(0, i) for i in range(n)] + [(i, 0) for i in range(1, m)])
        seenP = set()
        bfs(queue, seenP)
        # bfs from all cells conected to the atlantic
        # keep track of seen nodes and teh results is the intersection with seen form pacific
        queue = deque([(m - 1, i) for i in range(n)] + [(i, n - 1) for i in range(m - 1)])
        seenA = set()
        bfs(queue, seenA)
        return list(seenP.intersection(seenA))
                