# title: Time Needed to Inform All Employees
# timestamp: 2025-06-04 17:55:29
# problemUrl: https://leetcode.com/problems/time-needed-to-inform-all-employees/
# memory: 39.1 MB
# runtime: 175 ms

class Solution:
    def numOfMinutes(self, n: int, headID: int, managers: List[int], informTime: List[int]) -> int:
        if n == 1:
            return 0
        subordinates = [[] for _ in range(n)]
        for sub, manager in enumerate(managers):
            if manager == -1:
                continue
            subordinates[manager].append(sub)
        
        queue = deque([(headID, 0)])
        time = 0
        
        while queue:
            manager, partialTime = queue.popleft()
            # if subordinates[manager]:
            time = max(time, partialTime + informTime[manager])
            
            for sub in subordinates[manager]:
                if not subordinates[sub]:
                    continue
                queue.append((sub, partialTime + informTime[manager]))
        
        return time