# title: Sum of k-Mirror Numbers
# timestamp: 2025-06-23 23:43:03
# problemUrl: https://leetcode.com/problems/sum-of-k-mirror-numbers/
# memory: 17.9 MB
# runtime: 2377 ms

class Solution:
    def kMirror(self, k: int, n: int) -> int:
        def createPalindrome(num, oddLen):
            rev = num
            if oddLen:
                rev //= 10
            while rev > 0:
                num = num * 10 + rev % 10
                rev //= 10
            return num

        def isPalindrome(num, base):
            digits = []
            while num > 0:
                digits.append(num % base)
                num //= base
            return digits == digits[::-1]
    
        total, length = 0, 1
        while n > 0:
            for oddLen in [True, False]:
                for i in range(length, length * 10):
                    if n <= 0:
                        break

                    p = createPalindrome(i, oddLen)
                    if isPalindrome(p, k):
                        total += p
                        n -= 1
        
            length *= 10
        
        return total
