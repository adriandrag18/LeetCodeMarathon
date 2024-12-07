# title: Digit Operations to Make Two Integers Equal
# timestamp: 2024-12-07 17:25:03
# problemUrl: https://leetcode.com/problems/digit-operations-to-make-two-integers-equal/
# memory: 19.2 MB
# runtime: 935 ms

class Solution:
    def minOperations(self, n: int, m: int) -> int:
        prime = [True] * 10000
        prime[1] = False
        for i in range(2, 9999):
            if not prime[i]:
                continue
            for j in range(2, 9999 // i + 1):
                prime[i * j] = False
        
        # print(*[i for i, isPrime in enumerate(prime) if isPrime])  

        if prime[n] or prime[m]:
            return -1
        
        def getNeighbors(n: int):
            neighbores = []
            if n % 10 > 0 and not prime[n - 1]:
                neighbores.append(n - 1)
            if n % 10 < 9 and not prime[n + 1]:
                neighbores.append(n + 1)
            
            if n // 10 == 0:
                return neighbores
            if n // 10 % 10 > 0 and not prime[n - 10]:
                neighbores.append(n - 10)
            if n // 10 % 10 < 9 and not prime[n + 10]:
                neighbores.append(n + 10)
            
            if n // 100 == 0:
                return neighbores
            if n // 100 % 10 > 0 and not prime[n - 100]:
                neighbores.append(n - 100)
            if n // 100 % 10 < 9 and not prime[n + 100]:
                neighbores.append(n + 100)
            
            if n // 1000 == 0:
                return neighbores
            if n // 1000 % 10 > 0 and not prime[n - 1000]:
                neighbores.append(n - 1000)
            if n // 1000 % 10 < 9 and not prime[n + 1000]:
                neighbores.append(n + 1000)
            
            return neighbores
        
        q = []
        heapq.heappush(q, (n, n))

        distances = {node: 10000000 for node in range(10000)}
        distances[n] = n

        visited = set()

        while q:
            distance, node = heapq.heappop(q)
            if node in visited:
                continue

            if node == m:
                return distance

            visited.add(node)
            
            # print(node, getNeighbors(node))
            for n in getNeighbors(node):
                new_dist = distance + n
                
                if new_dist < distances[n]:
                    distances[n] = new_dist
                    if n not in visited:
                        heapq.heappush(q, (new_dist, n))
                    
                # print('\t', n, new_dist, distances[n], q)
            # print()

        return distances[m] if distances[m] != 10000000 else -1
