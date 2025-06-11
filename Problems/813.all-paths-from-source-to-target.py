# title: All Paths From Source to Target
# timestamp: 2025-06-02 11:53:58
# problemUrl: https://leetcode.com/problems/all-paths-from-source-to-target/
# memory: 19.4 MB
# runtime: 6 ms

class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        n = len(graph)
        finished = []

        # paths = [[0]]
        # while paths:
        #     new = []
        #     for path in paths:
        #         node = path[-1]
        #         for next in graph[node]:
        #             if next == n - 1:
        #                 finished.append(path.copy() + [next])
        #                 continue
        #             new.append(path.copy() + [next])
        #     paths = new

        def dfs(path, node):
            path.append(node)
            
            if node == n - 1:
                finished.append(path.copy())
            else:
                for nextNode in graph[node]:
                    dfs(path, nextNode)

            path.pop()
        
        dfs([], 0)
        return finished