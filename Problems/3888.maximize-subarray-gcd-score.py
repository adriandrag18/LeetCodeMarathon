# title: Maximize Subarray GCD Score
# timestamp: 2025-06-08 01:00:18
# problemUrl: https://leetcode.com/problems/maximize-subarray-gcd-score/
# memory: 18.1 MB
# runtime: 4634 ms

class Solution:
    def maxGCDScore(self, nums: List[int], k: int) -> int:
        def gcd(a, b):
            if a < b:
                a, b = b, a

            while b:
                a, b = b, a % b
            
            return a
        
        bin = []
        for num in nums:
            curr = 0
            while num % 2 == 0:
                curr += 1
                num //= 2
            bin.append(curr)

        n = len(nums)
        _max = n if k < bin.count(0) else 2 * n
        if k < bin.count(0):
            # slindinf window
            l = 0
            curr = 0
            for r in range(n):
                if not bin[r]:
                    curr += 1
                while curr > k:
                    if not bin[l]:
                        curr -= 1
                    l += 1
                _max = max(_max, 2 * (r - l + 1))

        for i in range(n):
            curr = nums[i]
            _max = max(_max,  2 * curr)
            b = defaultdict(int)
            b[bin[i]] = 1
            _min = bin[i]
            for j in range(i + 1, n):
                curr = gcd(curr, nums[j])
                b[bin[j]] += 1
                _min = min(_min, bin[j])
                double = 1
                if b[_min] <= k:
                    double = 2
                _max = max(_max, double * curr * (j - i + 1))
                if curr == 1:
                    break
        
        return _max