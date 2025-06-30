# title: Sort Items by Groups Respecting Dependencies
# timestamp: 2025-06-30 15:14:29
# problemUrl: https://leetcode.com/problems/sort-items-by-groups-respecting-dependencies/
# memory: 37.7 MB
# runtime: 87 ms

class Solution:
    def sortItems(self, n: int, m: int, group: List[int], beforeItems: List[List[int]]) -> List[int]:
        groups = [[] for _ in range(m + 1)]
        for i, g in enumerate(group):
            groups[g+1].append(i)
        
        indegree = [0] * n
        graph = [[] for _ in range(n)]
        for node, li in enumerate(beforeItems):
            indegree[node] += len(li)
            for i in li:
                graph[i].append(node)
        
        queue = deque([])
        for i in range(n):
            if not indegree[i]:
                queue.append((i, -1))

        def help(gr):
            nonlocal indegree, group, queue, topo

            ind = defaultdict(int)
            gNo = group[gr[0]]

            q = deque([])
            for el in gr:
                if indegree[el] == 0:
                    q.append(el)
            # print(gr, q)
            count = 0
            top = []
            while q:
                el = q.popleft()
                top.append(el)
                for next in graph[el]:
                    indegree[next] -= 1
                    ind[next] += 1
                    if indegree[next] == 0:
                        if gNo != -1 and group[next] == gNo:
                            q.append(next)
                        else:
                            queue.append((next, len(topo)))
                            count += 1

            # print(top)       
            if len(top) != len(gr):
                for k, v in ind.items():
                    indegree[k] += v
                for _ in range(count):
                    queue.pop()
                
                return []
            
            return top
        # print(queue)
        topo = []
        seen = set()
        while queue:
            el, check = queue.popleft()
            if el in seen:
                continue
            if len(topo) == check:
                return []
            
            gr = groups[group[el] + 1]
            if group[el] == -1:
                gr = [el]
            top = help(gr)
            
            if not top:
                queue.append((el, len(topo)))
                continue
            
            topo.extend(top)
            for el in top:
                seen.add(el)

        if len(topo) != n:
            return []

        return topo

# 0 -1 []
# 1 -1 [6]
# 2  1 [5]
# 3  0 [6]
# 4  0 [3]
# 5  1 []
# 6  0 [4]
# 7 -1 []