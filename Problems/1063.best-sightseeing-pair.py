# title: Best Sightseeing Pair
# timestamp: 2024-12-27 19:30:27
# problemUrl: https://leetcode.com/problems/best-sightseeing-pair/
# memory: 23 MB
# runtime: 8443 ms

class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        ans = 0
        print(len(values))
        for i, val in enumerate(values):
            for j in range(1, 1000 - ans + val):
                if i + j >= len(values):
                    break
                ans = max(ans, val + values[i + j] - j)

        return ans