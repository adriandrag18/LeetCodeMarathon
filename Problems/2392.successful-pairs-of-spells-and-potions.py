# title: Successful Pairs of Spells and Potions
# timestamp: 2024-12-30 16:11:16
# problemUrl: https://leetcode.com/problems/successful-pairs-of-spells-and-potions/
# memory: 38.9 MB
# runtime: 561 ms

class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        def binSearch(t):
            l, r = 0, m - 1
            while l <= r:
                mid = (l + r) // 2
                if potions[mid] < t:
                    l = mid + 1
                    continue
                r = mid - 1
            return m - r - 1

        n, m = len(spells), len(potions)
        potions.sort()
        return [binSearch(success / spell) for spell in spells]