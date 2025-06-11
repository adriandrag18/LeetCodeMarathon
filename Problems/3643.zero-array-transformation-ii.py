# title: Zero Array Transformation II
# timestamp: 2025-05-22 16:54:51
# problemUrl: https://leetcode.com/problems/zero-array-transformation-ii/
# memory: 63.8 MB
# runtime: 140 ms

class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        def isZeroArray(k) -> bool:
            freq = [0] * (len(nums) + 1)
            for q in queries[:k]:
                freq[q[0]] += q[2]
                freq[q[1]+1] -= q[2]
            
            pSum = 0
            for i, n in enumerate(nums):
                pSum += freq[i]
                if pSum < n:
                    return False
            
            return True

        if max(nums) == 0:
            return 0

        # res = len(queries) + 1
        # l, r = 0, len(queries)
        # while l <= r:
        #     m = (l + r) // 2
        #     if isZeroArray(m):
        #         r = m - 1
        #         res = min(res, m)
        #         continue
        #     l = m + 1

        # return res if res != len(queries) + 1 else -1

        n = len(nums)
        prefix = [0] * (n + 1)
        k, total = 0, 0
        for i in range(n):
            while total + prefix[i] < nums[i]:
                # add a query
                if k >= len(queries):
                    return -1
                
                left, right, val = queries[k]
                k += 1
                if right < i:
                    # print(i, k, prefix)
                    continue
                
                left = max(i, left)
                prefix[left] += val
                prefix[right + 1] -= val
            
            total += prefix[i]

        return k
