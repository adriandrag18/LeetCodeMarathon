# title: Minimum Array End
# timestamp: 2024-11-10 00:10:16
# problemUrl: https://leetcode.com/problems/minimum-array-end/
# memory: 16.8 MB
# runtime: 0 ms

class Solution:
    def minEnd(self, n: int, x: int) -> int:
        nb, xb = bin(n-1)[2:], [c for c in bin(x)[2:]]
        j = len(nb) - 1
        print(nb, xb)
        for i in range(len(xb) - 1, -1, -1):
            if xb[i] == '0':
                xb[i] = nb[j]
                j -= 1
                if j == -1:
                    break
        else:
            xb = [c for c in nb[:j+1]] + xb
        print(xb)
        return int(''.join(xb), 2)