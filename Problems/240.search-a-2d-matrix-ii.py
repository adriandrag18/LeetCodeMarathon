# title: Search a 2D Matrix II
# timestamp: 2024-12-12 18:05:24
# problemUrl: https://leetcode.com/problems/search-a-2d-matrix-ii/
# memory: 23.7 MB
# runtime: 148 ms

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        l, r = 0, m - 1
        i = 0
        while l <= r:
            i+=1
            if i == 1000:
                print("Loop")
                return False
            mid = (l + r) // 2
            # print(l, mid, r)
            if matrix[mid][0] == target:
                return True
            if  matrix[mid][0] > target:
                r = mid - 1
                continue
            if matrix[mid][n-1] == target:
                return True
            if matrix[mid][n-1] > target:
                r = mid - 1
                continue
            l = mid + 1
        # print(l)
        i = l
        while i < m:
            # print(i)
            if matrix[i][0] > target:
                break
            if matrix[i][n-1] < target:
                i += 1
                continue
            
            l, r = 0, n - 1
            while l <= r:
                mid = (l + r) // 2
                if matrix[i][mid] == target:
                    return True
                if matrix[i][mid] > target:
                    r = mid - 1
                    continue
                l = mid + 1
            i += 1
        
        return False