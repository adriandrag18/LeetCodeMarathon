# title: Evaluate Division
# timestamp: 2025-01-06 17:20:26
# problemUrl: https://leetcode.com/problems/evaluate-division/
# memory: 18 MB
# runtime: 0 ms

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        results = {}
        for val, eq in zip(values, equations):
            a, b = eq
            results[a] = results.get(a, {})
            results[a][b] = val
            results[b] = results.get(b, {})
            results[b][a] = 1 / val
        n = len(results)

        res = []
        for q in queries:
            x, y = q
            if x == y:
                res.append(1 if x in results else -1)
                continue
            seen = set()
            seen.add(x)
            queue = deque([(x, 1)])
            r = -1
            while queue:
                n, prod = queue.popleft()
                if n not in results:
                    break
                for node, val in results[n].items():
                    if node == y:
                        r = prod * val
                        queue.clear()
                        break
                    if node in seen:
                        continue
                    queue.append((node, prod * val))
                    seen.add(node)
            res.append(r)
        
        return res 
