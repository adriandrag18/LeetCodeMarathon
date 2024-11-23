# title: Stone Removal Game
# timestamp: 2024-11-23 16:36:08
# problemUrl: https://leetcode.com/problems/stone-removal-game/
# memory: 16.7 MB
# runtime: 0 ms

class Solution:
    def canAliceWin(self, n: int) -> bool:
        k = 10
        winAlice = True
        while k > 0:
            n -= k
            if n < 0:
                return not winAlice
            k-=1
            winAlice = not winAlice

        return not winAlice