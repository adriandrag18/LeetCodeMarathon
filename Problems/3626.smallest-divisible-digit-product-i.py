# title: Smallest Divisible Digit Product I
# timestamp: 2024-11-16 15:42:14
# problemUrl: https://leetcode.com/problems/smallest-divisible-digit-product-i/
# memory: 16.8 MB
# runtime: 0 ms

class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        # def isPrime(n):
        #     if n % 2 == 0:
        #         return False
        #     i = 3
        #     while i * i <= n:
        #         if n % i == 0:
        #             return False
        #         i += 2
        #     return True
        
        # factors = []
        # if t % 2 == 0:
        #     factors.append(2)
        # i = 3
        # while i * i < t:
        #     if n % i == 0 and isPrime(i):
        #         factors.append(i)
        #     i += 2
        
        # if factors[-1] > 9:
        #     return F

        # if t == 10:
        #     return ((n - 1) // 10 + 1) * 10
        # if n == 100:
        #     return 110 + t
        for i in range(n, 200):
            s = i % 10
            if i // 10: s *= (i // 10) % 10
            if s % t == 0:
                return i
        return -1