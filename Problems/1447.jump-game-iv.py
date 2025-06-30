# title: Jump Game IV
# timestamp: 2025-06-19 14:28:35
# problemUrl: https://leetcode.com/problems/jump-game-iv/
# memory: 37.1 MB
# runtime: 153 ms

class Solution:
    def minJumps(self, arr: List[int]) -> int:
        n = len(arr)
        if n == 1:
            return 0

        map = {}
        for i, el in enumerate(arr):
            if el not in map:
                map[el] = []
            map[el].append(i)
        
        seen = set([0])
        seenVals = set()
        q = deque([(0, 0)])
        while q:
            index, depth = q.popleft()
            
            neib = map[arr[index]][::-1] if arr[index] not in seenVals else []
            if index + 1 < n:
                neib.append(index + 1)
            if index > 0:
                neib.append(index - 1)
            
            seenVals.add(arr[index])
            
            for i in neib:
                if i == n - 1:
                    return depth + 1
                if i not in seen:
                    seen.add(i)
                    q.append((i, depth + 1))
        
        return 0