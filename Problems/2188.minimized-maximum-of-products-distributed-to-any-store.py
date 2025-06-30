# title: Minimized Maximum of Products Distributed to Any Store
# timestamp: 2024-11-14 12:22:34
# problemUrl: https://leetcode.com/problems/minimized-maximum-of-products-distributed-to-any-store/
# memory: 28.6 MB
# runtime: 479 ms

import bisect

class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        l, r = 1, max(quantities)
        while l <= r:
            m = (l + r) // 2
            s = sum([(q - 1) // m + 1 for q in quantities])
            if n >= s:
                r = m - 1
                continue
            l = m + 1
    
        return r + 1