# title: Minimum Time to Repair Cars
# timestamp: 2025-03-17 23:34:09
# problemUrl: https://leetcode.com/problems/minimum-time-to-repair-cars/
# memory: 22 MB
# runtime: 875 ms

class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        def helper(n):
            count = 0
            for r in ranks:
                count += int(sqrt(n / r))
                # print(f'\t{n / r} {int(sqrt(n / r))}, {count}')
            
            return cars <= count
        
        l, r = 1, max(ranks) * cars * cars
        while l <= r:
            m = (l + r) // 2
            # print(m)
            if helper(m):
                r = m - 1
            else:
                l = m + 1
        
        return l
                