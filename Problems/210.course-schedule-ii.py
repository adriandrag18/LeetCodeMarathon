# title: Course Schedule II
# timestamp: 2025-06-02 15:16:34
# problemUrl: https://leetcode.com/problems/course-schedule-ii/
# memory: 18.8 MB
# runtime: 0 ms

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # adjList = [[] for _ in range(numCourses)]
        # for edge in prerequisites:
        #     adjList[edge[0]].append(edge[1])
        
        # def dfs(path, node):
        #     if node in path:
        #         return False
        #     if node in seen:
        #         return True
            
        #     path.add(node)
        #     for n in adjList[node]:
        #         if not dfs(path, n):
        #             return False
            
        #     seen.add(node)
        #     result.append(node)
        #     path.remove(node)

        #     return True
        
        # seen, result = set(), []
        # for node in range(numCourses):
        #     if not dfs(set(), node):
        #         return []
        
        indegree = [0] * numCourses
        adjList = [[] for _ in range(numCourses)]
        for course, pre in prerequisites:
            indegree[pre] += 1
            adjList[course].append(pre)
        
        result = []
        queue = deque([])
        for course in range(numCourses):
            if indegree[course] == 0:
                queue.append(course)

        while queue:
            node = queue.popleft()
            result.append(node)

            for next in adjList[node]:
                indegree[next] -= 1
                if indegree[next] == 0:
                    queue.append(next)
        
        if len(result) < numCourses:
            return []

        return result[::-1]