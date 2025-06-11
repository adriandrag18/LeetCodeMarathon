# title: Maximize Y‑Sum by Picking a Triplet of Distinct X‑Values
# timestamp: 2025-06-07 18:57:23
# problemUrl: https://leetcode.com/problems/maximize-ysum-by-picking-a-triplet-of-distinct-xvalues/
# memory: 48.6 MB
# runtime: 168 ms

class Solution:
    def maxSumDistinctTriplet(self, x: List[int], y: List[int]) -> int:
        n = len(x)
        valueY = {}
        for i in range(n):
            if x[i] in valueY:
                valueY[x[i]].append(y[i])
            else:
                valueY[x[i]] = [y[i]]

        for v in valueY:
            valueY[v] = max(valueY[v])

        if len(valueY) < 3:
            return -1

        values = sorted(valueY.values(), reverse=True)
        return sum(values[:3])