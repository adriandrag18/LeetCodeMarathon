# title: Zero Array Transformation III
# timestamp: 2025-05-23 00:20:27
# problemUrl: https://leetcode.com/problems/zero-array-transformation-iii/
# memory: 61.9 MB
# runtime: 279 ms

class Solution:
    def maxRemoval(self, nums: List[int], queries: List[List[int]]) -> int:
        n = len(nums)
        
        usedQuery = []
        availableQuery = []

        queries.sort(key=lambda x: x[0])
        qPos = 0
        count = 0

        for i in range(n):
            while qPos < len(queries) and queries[qPos][0] == i:
                heapq.heappush(availableQuery, -queries[qPos][1])
                qPos += 1

            nums[i] -= len(usedQuery)

            while nums[i] > 0 and availableQuery and -availableQuery[0] >= i:
                heapq.heappush(usedQuery, -heapq.heappop(availableQuery))
                nums[i] -= 1
                count += 1

            if nums[i] > 0:
                return -1

            while usedQuery and usedQuery[0] == i:
                heapq.heappop(usedQuery)

        return len(queries) - count