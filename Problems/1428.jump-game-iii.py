# title: Jump Game III
# timestamp: 2025-06-19 13:50:30
# problemUrl: https://leetcode.com/problems/jump-game-iii/
# memory: 22.8 MB
# runtime: 11 ms

class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        n = len(arr)
        seen = set([start])
        q = deque([start])
        while q:
            index = q.popleft()
            for i in [index - arr[index], index + arr[index]]:
                if 0 <= i < n:
                    if arr[i] == 0:
                        return True
                    if i not in seen:
                        seen.add(i)
                        q.append(i)
        
        return False
