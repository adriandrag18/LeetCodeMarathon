# title: Total Cost to Hire K Workers
# timestamp: 2025-01-06 12:38:43
# problemUrl: https://leetcode.com/problems/total-cost-to-hire-k-workers/
# memory: 27 MB
# runtime: 175 ms

class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        max = 10**6
        heap, heapR = costs[0:candidates], costs[candidates:]
        if 2 * candidates < len(costs):
            heapR = costs[len(costs)-candidates:]
        heapq.heapify(heap)
        heapq.heapify(heapR)

        l, r = candidates, len(costs) - candidates - 1
        cost = 0
        while heap and heapR and k:
            # print(cost, heap, heapR)
            elL, elR = heappop(heap), heappop(heapR)
            if elR < elL:
                heappush(heap, elL)
                cost += elR
                if l <= r:
                    heappush(heapR, costs[r])
                    r -= 1
                k -= 1
                continue
            heappush(heapR, elR)
            cost += elL
            if l <= r:
                heappush(heap, costs[l])
                l += 1
            k -= 1
        
        while heap and k:
            cost += heappop(heap)
            k -= 1
        
        while heapR and k:
            cost += heappop(heapR)
            k -= 1

        return cost