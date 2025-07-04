# title: Prime Subtraction Operation
# timestamp: 2024-11-11 17:54:07
# problemUrl: https://leetcode.com/problems/prime-subtraction-operation/
# memory: 16.7 MB
# runtime: 47 ms

class Solution:
    def primeSubOperation(self, nums: List[int]) -> bool:
        isPrime = [True] * (max([2, *nums]) + 1)
        isPrime[0] = False
        isPrime[1] = False
        for i, prime in enumerate(isPrime):
            if not prime:
                continue
            j = 2 * i
            while j < len(isPrime):
                isPrime[j] = False
                j += i
        
        prevPrime = [0] * len(isPrime)
        for i in range(1, len(isPrime)):
            prevPrime[i] = i-1 if isPrime[i-1] else prevPrime[i-1]

        nums[0] -= prevPrime[nums[0]]
        for i in range(1, len(nums)):
            if nums[i] - nums[i-1] <= 0:
                return False
            nums[i] -= prevPrime[nums[i] - nums[i-1]]
            
        return True