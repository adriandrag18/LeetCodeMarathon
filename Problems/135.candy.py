# title: Candy
# timestamp: 2025-06-02 11:37:49
# problemUrl: https://leetcode.com/problems/candy/
# memory: 19.9 MB
# runtime: 12 ms

class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        candies = [1] * n
        res = 1
        up = down = peak = 0

        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                peak = up = up + 1
                res += up + 1
                down = 0
            elif ratings[i] < ratings[i - 1]:
                down += 1
                res += down + 1 if down > peak else down
                up = 0
            else:
                res += 1
                up = down = peak = 0

        return res