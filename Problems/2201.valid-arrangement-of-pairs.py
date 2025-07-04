# title: Valid Arrangement of Pairs
# timestamp: 2024-12-01 00:58:04
# problemUrl: https://leetcode.com/problems/valid-arrangement-of-pairs/
# memory: 84.4 MB
# runtime: 305 ms

class Solution:
    def validArrangement(self, pairs: List[List[int]]) -> List[List[int]]:
        # graph represents adjacency list, inOutDeg tracks in/out degree difference
        graph = defaultdict(list)
        inOutDeg = defaultdict(int)

        # Build graph and count in/out degrees
        for start, end in pairs:
            graph[start].append(end)
            inOutDeg[start] += 1  # out-degree
            inOutDeg[end] -= 1    # in-degree

        # Find starting node 
        startNode = pairs[0][0] 
        for node in inOutDeg:
            if inOutDeg[node] == 1:
                startNode = node
                break

        path = []
        def dfs(curr):
            while graph[curr]:
                nextNode = graph[curr].pop()
                dfs(nextNode)
                path.append((curr, nextNode))

        dfs(startNode)
        return path[::-1]
        