# title: Car Fleet
# timestamp: 2024-11-08 05:44:07
# problemUrl: https://leetcode.com/problems/car-fleet/
# memory: 36.7 MB
# runtime: 166 ms

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed), reverse=True)
        res, prev = 0, -1
        for p, s in cars:
            curr = (target - p) / s
            if curr > prev:
                prev = curr
                res += 1
        return res