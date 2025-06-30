# title: Most Profitable Path in a Tree
# timestamp: 2025-02-24 14:50:25
# problemUrl: https://leetcode.com/problems/most-profitable-path-in-a-tree/
# memory: 77.7 MB
# runtime: 335 ms

class Solution:
    def mostProfitablePath(self, edges: List[List[int]], bob: int, amount: List[int]) -> int:
        adjList = [[] for _ in amount]
        for edge in edges:
            adjList[edge[0]].append(edge[1])
            adjList[edge[1]].append(edge[0])
        # print(*adjList, sep='\n')

        bobPath = []
        def findBobPath(node, seen):
            nonlocal bobPath, bob
            if node == bob:
                bobPath.append(node)
                return True

            seen[node] = True
            for n in adjList[node]:
                if seen[n]:
                    continue
                if findBobPath(n, seen):
                    bobPath.append(node)
                    return True
            
            seen[node] = False
            return False

        findBobPath(0, [False] * len(amount))
        # bobPath = {node: i for i, node in enumerate(bobPath)}
        print(bobPath)
        if len(bobPath) % 2 == 1:
            amount[bobPath[len(bobPath) // 2]] //= 2
        for n in bobPath[:len(bobPath) // 2]:
            amount[n] = 0
        print(amount)

        def findAliceMax(node, seen, depth):
            seen[node] = True
            results = [findAliceMax(n, seen, depth + 1) for n in adjList[node] if not seen[n]]
            m = max(results) if results else 0
            # print(node, m, depth, bobPath[node] if node in bobPath else 'Not in bob path', end=' ')
            m += amount[node]
            seen[node] = False
            # print(m)
            return m

        return findAliceMax(0, [False] * len(amount), 0)
            
            