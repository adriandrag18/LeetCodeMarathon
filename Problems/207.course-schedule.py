# title: Course Schedule
# timestamp: 2025-06-02 14:10:46
# problemUrl: https://leetcode.com/problems/course-schedule/
# memory: 19.7 MB
# runtime: 3 ms

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        seen = set()
        adjList = [[] for _ in range(numCourses)]
        for edge in prerequisites:
            adjList[edge[0]].append(edge[1])
        
        def dfs(path, node):
            if node in path:
                return False
            if node in seen:
                return True
            
            seen.add(node)
            path.add(node)
            for n in adjList[node]:
                if not dfs(path, n):
                    return False
            path.remove(node)
            return True
        
        for node in range(numCourses):
            if not dfs(set(), node):
                return False
        
        return True