# title: Number of Provinces
# timestamp: 2025-01-06 16:34:51
# problemUrl: https://leetcode.com/problems/number-of-provinces/
# memory: 18.8 MB
# runtime: 5 ms

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        def getNeighbers(n):
            return [i for i, connected in enumerate(isConnected[n]) if connected and not seen[i]]

        seen = [False] * n
        count = 0
        for i in range(n):
            if seen[i]:
                continue
            count += 1
            seen[i] = True
            queue = deque([i])
            while queue:
                n = queue.popleft()
                # print(n, getNeighbers(n))
                for node in getNeighbers(n):
                    queue.append(node)
                    seen[node] = True
        
        return count