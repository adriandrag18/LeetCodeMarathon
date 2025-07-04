# title: Find the K-th Character in String Game II
# timestamp: 2025-07-04 11:15:37
# problemUrl: https://leetcode.com/problems/find-the-k-th-character-in-string-game-ii/
# memory: 17.9 MB
# runtime: 0 ms

class Solution:
    def kthCharacter(self, k: int, operations: List[int]) -> str:
        return chr(ord('a') + (sum([1 for c, op in zip(reversed(bin(k-1)[2:]), operations) if c == '1' and op == 1]) % 26))

