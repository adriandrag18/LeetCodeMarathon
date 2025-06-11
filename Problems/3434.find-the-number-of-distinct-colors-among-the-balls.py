# title: Find the Number of Distinct Colors Among the Balls
# timestamp: 2025-02-07 15:53:34
# problemUrl: https://leetcode.com/problems/find-the-number-of-distinct-colors-among-the-balls/
# memory: 63.1 MB
# runtime: 71 ms

class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        arr = {}
        map = {-1: limit + 2}
        # print(len(queries))
        count = 0
        res = []
        for x, y in queries:
            # print(x, y)
            if x in arr:
                map[arr[x]] -= 1
                if map[arr[x]] == 0:
                    count -= 1
            
            arr[x] = y
            # print(y not in map,  map[y] if y in map else 0)
            if y not in map or map[y] < 1:
                count += 1
                map[y] = 0
            map[y] += 1

            res.append(count)
            # print(arr)
            # print(res)
            # print()

        return res