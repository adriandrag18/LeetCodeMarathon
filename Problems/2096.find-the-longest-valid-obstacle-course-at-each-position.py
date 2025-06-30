# title: Find the Longest Valid Obstacle Course at Each Position
# timestamp: 2025-06-30 11:11:50
# problemUrl: https://leetcode.com/problems/find-the-longest-valid-obstacle-course-at-each-position/
# memory: 34.8 MB
# runtime: 117 ms

class Solution:
    def longestObstacleCourseAtEachPosition(self, obstacles: List[int]) -> List[int]:
        dp = [obstacles[0]]
        res = [1]
        for o in obstacles[1:]:
            if dp[-1] <= o:
                dp.append(o)
                res.append(len(dp))
            else:
                i = bisect_right(dp, o)
                dp[i] = o
                res.append(i + 1)
        
        return res
