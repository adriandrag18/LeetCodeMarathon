# title: Shift Distance Between Two Strings
# timestamp: 2024-11-23 17:08:38
# problemUrl: https://leetcode.com/problems/shift-distance-between-two-strings/
# memory: 18 MB
# runtime: 432 ms

class Solution:
    def shiftDistance(self, s: str, t: str, nextCost: List[int], previousCost: List[int]) -> int:
        nextCostDP = [[0] * len(nextCost) for _ in range(26)]
        previousCostDP = [[0] * len(nextCost) for _ in range(26)]

        for i in range(1, 26):
            for j in range(0, 26):
                nextCostDP[i][j] = nextCostDP[i-1][j] + nextCost[i + j - 27]
        
        # print(*nextCostDP, sep='\n')
        
        for i in range(1, 26):
            for j in range(0, 26):
                previousCostDP[i][j] = previousCostDP[i-1][j] + previousCost[j - i + 1]
        
        # print(*previousCostDP, sep='\n')

        cost = 0
        for a, b in zip(s, t):
            ia = ord(a) - ord('a')
            ib = ord(b) - ord('a')
            dif = (ia - ib + 26) % 26
            # print(a, b, ia, ib, dif, end=' ')
            cost += min(nextCostDP[-dif][ia], previousCostDP[dif][ia])
            # print(nextCostDP[-dif][ia], previousCostDP[dif][ia], cost)
        
        return cost