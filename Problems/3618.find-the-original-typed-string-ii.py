# title: Find the Original Typed String II
# timestamp: 2025-07-02 15:08:04
# problemUrl: https://leetcode.com/problems/find-the-original-typed-string-ii/
# memory: 29.7 MB
# runtime: 2633 ms

class Solution:
    def possibleStringCount(self, word: str, k: int) -> int:
        mod = 10**9 + 7
        n = len(word)

        if k > n:
            return 0
        if k == n:
            return 1

        prev = ''
        count = 1
        li = []
        for c in word:
            if c == prev:
                count += 1
            else:
                li.append(count)
                count = 1
                prev = c
        li.append(count)
        li = li[1:]
        m = len(li)

        total = reduce(lambda x, y: (x * y) % mod, li)

        if k <= m:
            return total 

        dp = [[0] * 2000, [0] * 2000]
        dp[0][0] = 1
        prefix = [0] * 2001

        for i in range(m):
            for j in range(k - m):
                prefix[j+1] = (prefix[j] + dp[i&1][j]) % mod
                l, r = max(0, j - li[i] + 1), j
                dp[(i+1)&1][j] = (prefix[r+1] - prefix[l] + mod) % mod
            
        less = 0
        for num in dp[m & 1]:
            less += num
            
        return (total - (less % mod) + mod) % mod
