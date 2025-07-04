# title: Angle Between Hands of a Clock
# timestamp: 2025-06-01 20:48:02
# problemUrl: https://leetcode.com/problems/angle-between-hands-of-a-clock/
# memory: 17.7 MB
# runtime: 0 ms

class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        hour %= 12
        hAngle = hour * 30 + minutes / 2
        mAngle = minutes * 6
        
        angle = hAngle - mAngle
        if angle < 0:
            angle = -angle
        if angle > 180:
            angle = 360 - angle
        
        return angle