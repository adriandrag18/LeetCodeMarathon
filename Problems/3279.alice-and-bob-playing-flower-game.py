# title: Alice and Bob Playing Flower Game
# timestamp: 2025-06-01 20:55:42
# problemUrl: https://leetcode.com/problems/alice-and-bob-playing-flower-game/
# memory: 17.6 MB
# runtime: 0 ms

class Solution:
    def flowerGame(self, n: int, m: int) -> int:
        return (n // 2) * ((m + 1) // 2) + ((n + 1) // 2) * (m // 2)