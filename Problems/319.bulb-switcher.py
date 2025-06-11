# title: Bulb Switcher
# timestamp: 2025-06-01 20:03:03
# problemUrl: https://leetcode.com/problems/bulb-switcher/
# memory: 17.7 MB
# runtime: 0 ms

class Solution:
    def bulbSwitch(self, n: int) -> int:
        i = 0
        while (i + 1) * (i + 1) <= n: i += 1
        return i