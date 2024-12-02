# title: Find Champion II
# timestamp: 2024-12-02 23:27:20
# problemUrl: https://leetcode.com/problems/find-champion-ii/
# memory: 18.1 MB
# runtime: 5 ms

class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        isUndefeated = [True] * n
        
        for winner, loser in edges:
            isUndefeated[loser] = False
            
        champion = -1
        championCount = 0
        
        for team in range(n):
            if isUndefeated[team]:
                champion = team
                championCount += 1
                
        if championCount == 1:
            return champion
            
        return -1