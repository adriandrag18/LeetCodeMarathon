# title: 01 Matrix
# timestamp: 2025-06-19 01:36:32
# problemUrl: https://leetcode.com/problems/01-matrix/
# memory: 28.5 MB
# runtime: 272 ms

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        visited = set()

        def dfs(i, j, dist):
            neib = []
            for ni, nj in [(i - 1, j), (i, j - 1), (i, j + 1), (i + 1, j)]:
                if 0 <= ni < m and 0 <= nj < n:
                    if mat[ni][nj] == 0:
                        dist = 1
                    else:
                        neib.append((ni, nj))
            
            mat[i][j] = min(mat[i][j], dist)
            visited.add((i, j))

            for ni, nj, in neib:
                if (ni, nj) in visited:
                    continue
                dfs(ni, nj, dist + 1)
            
            new = []
            while neib:
                for i, j in neib:
                    if mat[i][j] > dist + 1:
                        mat[i][j] = dist + 1    
                        for ni, nj in [(i - 1, j), (i, j - 1), (i, j + 1), (i + 1, j)]:
                            if 0 <= ni < m and 0 <= nj < n:
                                if (ni, nj) == (0, 6):
                                    debug = True
                                new.append((ni, nj))
                neib, new = new, []
                dist += 1
        
        for i in range(m):
            for j in range(n):
                if mat[i][j]:
                    mat[i][j] = float('inf')
        
        for i in range(m):
            for j in range(n):
                if mat[i][j] and (i, j) not in visited:
                    dfs(i, j, mat[i][j])
            
        return mat
                