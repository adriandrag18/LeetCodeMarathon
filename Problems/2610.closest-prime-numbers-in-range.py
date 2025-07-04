# title: Closest Prime Numbers in Range
# timestamp: 2025-03-09 21:21:27
# problemUrl: https://leetcode.com/problems/closest-prime-numbers-in-range/
# memory: 28.3 MB
# runtime: 1856 ms

maxNum = 10** 6 + 1
class Solution:
    isPrime = [True] * (maxNum)
    def closestPrimes(self, left: int, right: int) -> List[int]:
        if self.isPrime[0]:
            self.isPrime[0] = False
            self.isPrime[1] = False

            for i in range(2, maxNum):
                if not self.isPrime[i]:
                    continue
                j = 2
                while i * j <  maxNum:
                    self.isPrime[i * j] = False
                    j += 1
        
        primes = [i for i, val in enumerate(self.isPrime) if val and left <= i <= right]
        if len(primes) < 2:
            return [-1, -1]
        
        pair = [-1, -1]
        res = maxNum
        for i in range(1, len(primes)):
            if primes[i] - primes[i - 1] < res:
                res = primes[i] - primes[i - 1]
                pair = [primes[i - 1], primes[i]]
        
        return pair

