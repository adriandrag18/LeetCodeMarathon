# title: Length of Longest Fibonacci Subsequence
# timestamp: 2025-02-27 15:40:39
# problemUrl: https://leetcode.com/problems/length-of-longest-fibonacci-subsequence/
# memory: 18 MB
# runtime: 827 ms

class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        n = len(arr)
        res = 0
        nums = set(arr)
        for i in range(n - 2):
            for j in range(i + 1, n - 1):
                count = 2
                a, b = arr[i], arr[j]
                while a + b in nums:
                    a, b = b, a + b
                    count += 1
                    res = max(res, count)

        return res
