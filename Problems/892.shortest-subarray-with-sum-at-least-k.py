# title: Shortest Subarray with Sum at Least K
# timestamp: 2024-11-17 04:23:26
# problemUrl: https://leetcode.com/problems/shortest-subarray-with-sum-at-least-k/
# memory: 31.8 MB
# runtime: 175 ms

class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        if max(nums) >= k:
            return 1
        sum, curr, res = 0, 0, len(nums) + 1
        q = deque([])
        for i, n in enumerate(nums):
            if n < 0:
                if sum + n <= 0:
                    q = deque([])
                    sum, curr = 0, 0
                    continue
                
                num, j = q.pop()
                n2 = n + num
                l2 = 1 + j
                while q and n2 < 0:
                    num, j = q.pop()
                    n2 += num
                    l2 += j
                q.append((n2, l2))
                sum += n
                curr += 1
            else:
                q.append((n, 1))
                sum += n
                curr += 1
            # print(q, sum, res, curr)
            while q and sum >= k:
                res = min(res, curr)
                n, l = q.popleft()
                sum -= n
                curr -= l
                # print(q, sum, res, curr)

        return res if res != len(nums) + 1 else -1