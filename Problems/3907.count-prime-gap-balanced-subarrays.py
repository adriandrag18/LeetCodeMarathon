# title: Count Prime-Gap Balanced Subarrays
# timestamp: 2025-06-21 19:34:32
# problemUrl: https://leetcode.com/problems/count-prime-gap-balanced-subarrays/
# memory: 24.2 MB
# runtime: 8290 ms

MAX = 5 * 10**4 + 1
isPrime = [True] * MAX

class Solution:
    def primeSubarray(self, nums: List[int], k: int) -> int:
        if isPrime[0]:
            isPrime[0] = isPrime[1] = False
            for num in range(2, MAX):
                if not isPrime[num]:
                    continue
                i = 2
                while i * num < MAX:
                    isPrime[i * num] = False
                    i += 1
                    
        n = len(nums)

        arr = []
        counts = []
        count = 1
        for num in nums:
            if isPrime[num]:
                arr.append(num)
                counts.append(count)
                count = 1
            else:
                count += 1
        counts.append(count)
        
        m = len(arr)
        
        minPrime = float('inf')
        maxPrime = 0
        minIndex = maxIndex = -1
        l, r = 0, 0
        res = 0
        
        for r in range(m):
            el = arr[r]
            a, b = minIndex, maxIndex
            if el <= minPrime:
                minPrime = el
                minIndex = r
            if el >= maxPrime:
                maxPrime = el
                maxIndex = r
                
            while r - l + 1 >= 2 and maxPrime - minPrime > k:
                el = arr[l]
                if minPrime == el and minIndex == l:
                    minPrime = float('inf')
                    for i in range(l + 1, r + 1):
                        if arr[i] < minPrime:
                            minPrime = arr[i]
                            minIndex = i
                if maxPrime == el and maxIndex == l:
                    maxPrime = 0
                    for i in range(l + 1, r + 1):
                        if arr[i] > maxPrime:
                            maxPrime = arr[i]
                            maxIndex = i
                l += 1
            
            if r - l + 1 >= 2:
                res += sum(counts[l:r]) * counts[r + 1]
                
        return res
        
        