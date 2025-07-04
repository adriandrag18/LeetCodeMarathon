# title: Minimum Increments to Equalize Leaf Paths
# timestamp: 2025-06-22 05:55:55
# problemUrl: https://leetcode.com/problems/minimum-increments-to-equalize-leaf-paths/
# memory: 76.2 MB
# runtime: 403 ms

class Solution:
    def minIncrease(self, n: int, edges: List[List[int]], cost: List[int]) -> int:
        adjList = defaultdict(list)
        for u, v in edges:
            adjList[u].append(v)
            adjList[v].append(u)

        sums = [0] * n

        def dfs(node, parent):
            s = 0
            for next in adjList[node]:
                if next == parent:
                    continue
                s = max(s, dfs(next, node))
            
            sums[node] = s + cost[node]
            
            return sums[node]

        maxSum = dfs(0, -1)
        
        count = 0

        def dfs2(node, parent, target):
            dif = target - sums[node]
            if dif:
                nonlocal count
                # print(node, target, sums[node])
                count += 1
            
            for next in adjList[node]:
                if next == parent:
                    continue
                dfs2(next, node, target - dif - cost[node])
            
        dfs2(0, -1, maxSum)
        
        return count
        