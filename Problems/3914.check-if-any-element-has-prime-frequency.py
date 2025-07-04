# title: Check if Any Element Has Prime Frequency
# timestamp: 2025-06-22 05:35:26
# problemUrl: https://leetcode.com/problems/check-if-any-element-has-prime-frequency/
# memory: 17.9 MB
# runtime: 0 ms

class Solution:
    def checkPrimeFrequency(self, nums: List[int]) -> bool:
        def isPrime(n):
            if n == 1:
                return False
            for i in range(2, n-1):
                if n % i == 0:
                    return False

            return True
        
        for k, v in Counter(nums).items():
            if isPrime(v):
                return True

        return False